def two_sum(nums: list[int], target: int) -> list[int]:
    """Return indices of two numbers adding up to target."""
    num_map = {} # Stores {number: index}
    
    for index, num in enumerate(nums):
        complement = target - num
        
        # Check if the complement has been seen
        if complement in num_map:
            return [num_map[complement], index]
            
        num_map[num] = index
        
    return []