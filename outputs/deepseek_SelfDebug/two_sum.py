def two_sum(nums: list[int], target: int) -> list[int]:
    """Return indices of the two numbers that add up to the target."""
    lookup = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in lookup:
            return [lookup[diff], i]
        lookup[num] = i
    return []
