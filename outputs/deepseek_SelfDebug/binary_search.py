def binary_search(arr: list[int], target: int) -> int:
    """Perform binary search on a sorted list to find the index of target."""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        value = arr[mid]
        if value == target:
            return mid
        elif value < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
