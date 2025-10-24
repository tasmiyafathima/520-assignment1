
def reverse_words_in_sentence(s: str) -> str:
    """Reverse the order of words in a sentence, but not the words themselves."""
    # Step 1: Split by spaces and remove extra ones
    words = s.strip().split()
    # Step 2: Reverse the list of words
    return " ".join(reversed(words))

