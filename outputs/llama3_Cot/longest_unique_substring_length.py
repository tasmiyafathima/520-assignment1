def longest_unique_substring_length(s: str) -> int:
    """Return the length of the longest substring without repeating characters."""
    char_map = {} # Stores the last seen index of each character
    max_length = 0
    left = 0 # Left boundary of the sliding window
    
    for right in range(len(s)):
        char = s[right]
        
        # If char is in the current window, shrink the window
        if char in char_map and char_map[char] >= left:
            left = char_map[char] + 1
            
        char_map[char] = right
        max_length = max(max_length, right - left + 1)
        
    return max_length