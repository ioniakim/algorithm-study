#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Longest Increasing Subsequence Algorithms을 다시 구현해 봄.
"""

class Lis(object):
    def __init__(self, seq):
        self._seq = seq

    def solve(self):
        m = 1

        for i in range(len(self._seq)):
            m = max(m, self._solve(i))
        return m

    def _solve(self, p):
        m = 0
        for i in range(p+1, len(self._seq)):
            if self._seq[p] < self._seq[i]:
                m = max(m, self._solve(i) + 1)
        return m


class LisDP(object):
    def __init__(self, seq):
        self._cache = [-1 for i in range(len(seq))]
        self._seq = seq

    def solve(self):
        m = 1
        for i in range(len(self._seq)):
            m = max(m, self._solve(i))
        return m

    def _solve(self, p):
        if self._cache[p] != -1:
            return self._cache[p]

        self._cache[p] = 1
        for nexti in range(p+1, len(self._seq)):
            if self._seq[p] < self._seq[nexti]:
                self._cache[p] = max(self._cache[p], self._solve(nexti) + 1)

        return self._cache[p]

seq = [5, 2, 3, 8, 4, 9]

def lis(p):
    m = 0
    for i in range(p+1, len(seq)):
        if seq[i] > seq[p]:
            m = max(m, 1 + lis(i))
    return m

# m = 0
# for i in range(len(seq)):
#     m = max(m, lis(i))

l = LisDP(seq)

print(l.solve())

seq = [5, 4, 3, 2, 1]

l = LisDP(seq)
print(l.solve())