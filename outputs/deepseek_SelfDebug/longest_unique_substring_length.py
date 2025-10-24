def longest_unique_substring_length(s: str) -> int:
    """Return the length of the longest substring without repeating characters."""
    start = 0
    seen = {}
    longest = 0
    for i, ch in enumerate(s):
        # If character was seen, move the start beyond its last index
        if ch in seen and seen[ch] >= start:
            start = seen[ch] + 1
        seen[ch] = i
        longest = max(longest, i - start + 1)
    return longest
