
def count_anagrams(words: list[str]) -> dict:
    """Group words that are anagrams and return counts per group."""
    groups = {}
    for w in words:
        key = tuple(sorted(w))
        groups[key] = groups.get(key, 0) + 1
    return groups
