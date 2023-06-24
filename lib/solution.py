import itertools

from functools import cache

class Solution:
    def __init__(self, v):
        self.m = max(max(k) for k in v) + 1
        self.v = v
    
    @cache
    def cap3(self, i, j, k):
        assert(0 <= i < j < k < self.m)

        small = [3 if (not self.v[(i, j, k)]) else 2]
        large = (self.cap3(j, l, k) + 1 for l in range(j + 1, k) if self.cap3(j, l, k) >= 3 and (not self.v[(i, j, l)]))
        stream = itertools.chain(small, large)
        return max(stream)

    @cache
    def cup3(self, i, j, k):
        assert(0 <= i < j < k < self.m)

        small = [3 if self.v[(i, j, k)] else 2]
        large = (self.cup3(i, l, j) + 1 for l in range(i + 1, j) if self.cup3(i, l, j) >= 3 and self.v[(l, j, k)])
        stream = itertools.chain(small, large)
        return max(stream)

    @cache
    def cap2(self, i, j):
        assert(0 <= i < j < self.m)
        return max(itertools.chain([2], (self.cap3(i, k, j) for k in range(i + 1, j))))
    
    @cache
    def cup2(self, i, j):
        assert(0 <= i < j < self.m)
        return max(itertools.chain([2], (self.cup3(i, k, j) for k in range(i + 1, j))))