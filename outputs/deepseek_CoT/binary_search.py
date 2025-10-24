
def merge_sorted_lists(a: list[int], b: list[int]) -> list[int]:
    """Merge two sorted lists into one sorted list."""
    i = j = 0
    merged = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:  
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    merged.extend(a[i:])
    merged.extend(b[j:])
    return merged
