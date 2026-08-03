"""Tests for the detection layer. stdlib unittest, so: python -m unittest discover -s tests"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from solstate.anomaly import MIN_HISTORY, detect, mad, median, robust_z   # noqa: E402
from solstate.config import DEFAULT_THRESHOLDS                            # noqa: E402

TH = dict(DEFAULT_THRESHOLDS)


class TestStatistics(unittest.TestCase):
    def test_median_odd_and_even(self):
        self.assertEqual(median([3, 1, 2]), 2)
        self.assertEqual(median([4, 1, 2, 3]), 2.5)
        self.assertEqual(median([]), 0.0)

    def test_mad_is_zero_for_constant_series(self):
        self.assertEqual(mad([5, 5, 5, 5]), 0.0)

    def test_mad_ignores_a_single_wild_outlier(self):
        # This is the whole reason MAD is used instead of stdev: one absurd
        # sample must not move the baseline. Contrast with a standard deviation,
        # which this same outlier inflates by three orders of magnitude.
        calm = [10, 10, 11, 9, 10, 10, 11, 9]
        polluted = calm + [10_000]
        self.assertLessEqual(mad(polluted), 1.5)
        self.assertEqual(median(calm), median(polluted))

        import statistics
        self.assertGreater(statistics.pstdev(polluted), 100 * statistics.pstdev(calm))

    def test_robust_z_needs_enough_history(self):
        self.assertIsNone(robust_z(5, [1, 2, 3]))
        self.assertIsNotNone(robust_z(5, [1, 2, 3, 4, 1, 2, 3, 4]))

    def test_robust_z_is_none_for_a_flat_history(self):
        # MAD is zero, so there is no honest z-score. Inventing one here is what
        # produced z=95 findings on 0.001% moves against live mainnet data.
        self.assertIsNone(robust_z(101.0, [100.0] * 10))

    def test_tiny_move_on_a_stable_metric_is_not_reported(self):
        # sol_total_supply barely moves between runs minutes apart; its MAD is
        # ~0 and any change is "statistically" enormous. It must stay quiet.
        hist = {"sol_total_supply": [631_500_000.0, 631_500_001.0] * 5}
        found = detect({"sol_total_supply": 631_500_002.0}, hist, TH)
        self.assertEqual(found, [])

    def test_a_genuinely_large_move_still_reports(self):
        hist = {"dex_volume_24h_usd": [1_000.0, 1_010.0, 990.0, 1_005.0,
                                       995.0, 1_000.0, 1_002.0, 998.0]}
        found = detect({"dex_volume_24h_usd": 5_000.0}, hist, TH)
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0].kind, "statistical")
        self.assertIn("% move", found[0].message)

    def test_statistical_findings_never_claim_critical(self):
        """Only rules encode what 'bad' means, so only rules may say critical."""
        hist = {"dex_volume_24h_usd": [1_000.0, 1_010.0, 990.0, 1_005.0,
                                       995.0, 1_000.0, 1_002.0, 998.0]}
        found = detect({"dex_volume_24h_usd": 500_000.0}, hist, TH)
        self.assertEqual(len(found), 1)
        self.assertGreater(abs(found[0].robust_z), 10 * TH["mad_z"])
        self.assertEqual(found[0].severity, "warning")

    def test_robust_z_flags_a_real_departure(self):
        hist = [100.0] * 4 + [102.0, 98.0, 101.0, 99.0]
        self.assertGreater(abs(robust_z(400, hist)), TH["mad_z"])
        self.assertLess(abs(robust_z(101, hist)), TH["mad_z"])


class TestRules(unittest.TestCase):
    def test_unhealthy_cluster_is_critical(self):
        found = detect({"health": "behind"}, {}, TH)
        self.assertTrue(any(a.metric == "health" and a.severity == "critical" for a in found))

    def test_healthy_cluster_is_silent(self):
        self.assertEqual(detect({"health": "ok"}, {}, TH), [])

    def test_tps_collapse_is_caught(self):
        hist = {"tps": [3000.0] * MIN_HISTORY}
        found = detect({"tps": 500.0}, hist, TH)
        self.assertTrue(any(a.metric == "tps" and a.severity == "critical" for a in found))

    def test_tps_within_band_is_silent(self):
        hist = {"tps": [3000.0] * MIN_HISTORY}
        self.assertEqual(detect({"tps": 2900.0}, hist, TH), [])

    def test_slow_slots_flagged(self):
        found = detect({"slot_time_ms": 1200.0}, {}, TH)
        self.assertTrue(any(a.metric == "slot_time_ms" for a in found))

    def test_delinquent_stake_escalates_to_critical(self):
        warn = detect({"delinquent_pct_by_stake": 6.0}, {}, TH)
        crit = detect({"delinquent_pct_by_stake": 25.0}, {}, TH)
        self.assertEqual([a.severity for a in warn], ["warning"])
        self.assertEqual([a.severity for a in crit], ["critical"])

    def test_price_and_tvl_bands(self):
        found = detect({"sol_change_24h_pct": -20.0, "tvl_change_24h_pct": 18.0}, {}, TH)
        self.assertEqual(len(found), 2)

    def test_a_rule_suppresses_the_duplicate_statistical_finding(self):
        # tps is handled by a rule; it must not also appear as a statistical hit.
        hist = {"tps": [3000.0] * 20}
        found = detect({"tps": 100.0}, hist, TH)
        self.assertEqual(sum(1 for a in found if a.metric == "tps"), 1)

    def test_booleans_are_not_treated_as_numbers(self):
        self.assertEqual(detect({"some_flag": True}, {"some_flag": [0.0] * 20}, TH), [])

    def test_findings_are_sorted_worst_first(self):
        found = detect(
            {"health": "behind", "slot_time_ms": 1200.0, "sol_change_24h_pct": -20.0}, {}, TH)
        self.assertEqual(found[0].severity, "critical")

    def test_missing_metrics_never_raise(self):
        self.assertEqual(detect({}, {}, TH), [])


class TestCounters(unittest.TestCase):
    """Monotonic counters must not be z-scored, or every run is a false critical."""

    def test_growing_counter_is_not_an_anomaly(self):
        hist = {"block_height": [100.0, 200.0, 300.0, 400.0,
                                 500.0, 600.0, 700.0, 800.0]}
        self.assertEqual(detect({"block_height": 900.0}, hist, TH), [])

    def test_epoch_progress_sawtooth_is_not_an_anomaly(self):
        # Climbs to ~100% then resets to ~0. A z-score screams at both ends.
        hist = {"epoch_progress_pct": [10.0, 25.0, 40.0, 55.0, 70.0, 85.0, 99.0, 99.5]}
        self.assertEqual(detect({"epoch_progress_pct": 0.4}, hist, TH), [])

    def test_counter_going_backwards_is_critical(self):
        hist = {"block_height": [500.0] * MIN_HISTORY}
        found = detect({"block_height": 400.0}, hist, TH)
        self.assertEqual([(a.metric, a.severity) for a in found],
                         [("block_height", "critical")])
        self.assertIn("backwards", found[0].message)

    def test_stalled_chain_counter_is_critical(self):
        hist = {"absolute_slot": [900.0] * MIN_HISTORY}
        found = detect({"absolute_slot": 900.0}, hist, TH)
        self.assertEqual([(a.metric, a.severity) for a in found],
                         [("absolute_slot", "critical")])
        self.assertIn("not advanced", found[0].message)

    def test_a_flat_epoch_number_is_normal(self):
        # An epoch lasts ~2 days, so it is flat across many runs. That must not
        # be reported as a stall the way a flat block height would be.
        hist = {"epoch": [1011.0] * MIN_HISTORY}
        self.assertEqual(detect({"epoch": 1011.0}, hist, TH), [])


if __name__ == "__main__":
    unittest.main()
