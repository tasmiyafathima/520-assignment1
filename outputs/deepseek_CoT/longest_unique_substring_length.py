
def longest_unique_substring_length(s: str) -> int:
    """Return the length of the longest substring without repeating characters (incorrect)."""
    start = 0
    seen = {}
    max_len = 0
    for i, ch in enumerate(s):
        if ch in seen and seen[ch] > start:
            start = seen[ch] + 1
        seen[ch] = i
        max_len = max(max_len, i - start + 1)
    return max_len
