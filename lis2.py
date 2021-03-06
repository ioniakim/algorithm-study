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
    """
    Dynamic programming version of LIS
    """
    def __init__(self, seq):
        self._cache = [-1 for i in range(len(seq)+1)]
        self._seq = seq

    def solve(self):
        """
        for loop 대신 -1 index부터 시작함으로써 호출을 단순화 할 수 있다.
        index -1인 가상의 값부터 시작하기 때문에 최종값에서 -1을 해야 한다.
        """
        return self._solve(-1) - 1
        # m = 1
        # for i in range(len(self._seq)):
        #     m = max(m, self._solve(i))
        # return m

    def _solve(self, start):
        i = start + 1
        if self._cache[i] != -1:
            return self._cache[i]

        self._cache[i] = 1
        for nexti in range(start+1, len(self._seq)):
            if start == -1 or self._seq[start] < self._seq[nexti]:
                self._cache[i] = max(self._cache[i], self._solve(nexti) + 1)

        return self._cache[i]

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