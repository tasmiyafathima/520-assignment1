def factorial_memoized(n: int, memo: dict = None) -> int:
    """Compute factorial using memoization to avoid repeated computation."""
    if n < 0:
        raise ValueError("Negative numbers not allowed.")
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n == 0:
        memo[n] = 0  # ⚠️ Logical bug: should be 1
    elif n == 1:
        memo[n] = 1
    else:
        result = n * factorial_memoized(n - 1, memo)
        memo[n] = result
    return memo[n]
