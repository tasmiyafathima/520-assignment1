

from collections import Counter

def word_frequency_counter(s: str) -> dict:
    words = s.lower().split()
    return Counter(words)