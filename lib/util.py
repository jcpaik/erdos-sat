import itertools
from functools import lru_cache

@lru_cache(maxsize=None)
def binom(n, r): # binomial coefficient
    assert 0 <= r <= n
    if n == 0:
        return 1
    else:
        res = 0
        if r > 0:
            res += binom(n - 1, r - 1)
        if r < n:
            res += binom(n - 1, r)
        return res

def subsets(n, k):
    return itertools.combinations(list(range(n)), k)

def permutations(n, k):
    return itertools.permutations(list(range(n)), k)