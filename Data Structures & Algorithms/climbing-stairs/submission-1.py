def _climbStairs(n, cache):
    if n in cache:
        return cache[n]

    if (n <= 0):
        ret = 0
    elif (n == 1):
        ret = 1
    elif (n == 2):
        ret = 2
    else:
        ret = _climbStairs(n-1, cache) + _climbStairs(n-2, cache)

    cache[n] = ret
    return ret

class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        return _climbStairs(n, cache)
