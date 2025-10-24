from collections import Counter

def word_frequency_counter(s: str) -> dict:
    """Return a dictionary counting frequency of each word (case-insensitive)."""
    return Counter(s.lower().split())