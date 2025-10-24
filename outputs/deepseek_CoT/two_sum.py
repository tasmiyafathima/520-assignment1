def two_sum(nums: list[int], target: int) -> list[int]:
    """Return indices of two numbers adding up to target."""
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
