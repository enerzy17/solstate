"""Data sources. Every collector returns a dict with 'metrics' and 'meta' keys,
where 'meta' carries one status record per probe so a partial failure is
visible in the output rather than silently absent.
"""
