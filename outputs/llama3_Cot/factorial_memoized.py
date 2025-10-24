def factorial_memoized(n: int, memo: dict = None) -> int:
    """Return factorial of n using memoization for efficiency."""
    if memo is None:
        memo = {}
        
    if n in memo:
        return memo[n]
        
    if n == 0:
        return 1
        
    result = n * factorial_memoized(n - 1, memo)
    memo[n] = result
    return result