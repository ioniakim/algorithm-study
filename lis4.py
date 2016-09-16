#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Lis4(object):
    def __init__(self):
        self.MAX = 101
        self._cache = [None for _ in range(self.MAX)]
        self._choices = [None for _ in range(self.MAX)]

    def solve(self, seq):
        self._seq = seq
        self._n = len(seq)
        self._init()
        return self._solve(-1)

    def reconstruct(self, start, seq):
        if start != -1:
            seq.append(self._choices[start+1])
        if self._choices[start + 1]:
            return self.reconstruct(self._choices[start + 1], seq)


    def _init(self):
        for i in range(self.MAX):
            self._cache[i] = None
            self._choices[i] = None
        pass

    def _solve(self, start):
        if self._cache[start+1]
            return self._cache[start+1]

        self._cache[start+1] = 1
        bestNext = -1
        for i in range(start+1, n ):
            if start == -1 || self._seq[start] < self._seq[i]:
                cand = 1 + self._solve(i)
                if cand > self._cache[start+1]:
                    self._cache[start+1] = cand
                    bestNext = i
        self._choices[start+1] = bestNext
        return self._cache[start+1]



def main():
    pass

if __name__ == '__main__':
    main()