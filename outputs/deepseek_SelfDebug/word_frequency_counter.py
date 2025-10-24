def word_frequency_counter(s: str) -> dict:
    """Count frequency of each word, ignoring case."""
    if not s.strip():
        return {}
    words = s.lower().split()
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    return counts
