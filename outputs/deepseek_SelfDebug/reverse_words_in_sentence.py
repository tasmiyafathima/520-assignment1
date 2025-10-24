def reverse_words_in_sentence(s: str) -> str:
    """Reverse the order of words in a sentence, keeping words intact."""
    # Remove leading/trailing spaces and split words
    words = [w for w in s.strip().split(" ") if w]
    # Reverse order of words
    reversed_words = words[::-1]
    # Join with single space
    return " ".join(reversed_words)
