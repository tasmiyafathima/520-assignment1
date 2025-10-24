def word_frequency_counter(s: str) -> dict:
    """Return a dictionary counting frequency of each word (case-insensitive)."""
    words = s.lower().split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq
