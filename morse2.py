#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Morse2(object):
    """
    이항계수를 이용해서 k
    """
    def __init__(self):
        self._bino = [[0 for j in range(201)] for i in range(201)]
        self._MAX = 1000000000 + 100
        self._calcBino()

    def _calcBino(self):
        for i in range(201):
            self._bino[i][0] = self._bino[i][i] = 1
            for j in range(201):
                self._bino[i][j] = min(self._MAX, self._bino[i-1][j] + self._bino[i-1][j-1])


    def morse(self, n, m, k):
        """
        k <= 1000000000
        """
        self._skip = k
        self._morse(n, m, "")

    def _morse(self, n, m, s):
        if self._skip < 0:
            return

        if 0 == n and 0 == m:
            if 0 == self._skip:
                print(s)
            self._skip -= 1

        if self._bino[n+m][n] <= self._skip:
            self._skip -= self._bino[n+m][n]
        if n > 0:
            self._morse(n-1, m, s + "-")
        if m > 0:
            self._morse(n, m-1, s + "o")

def main():
    m = Morse2()

    m.morse(100, 100, 10000)


if __name__ == '__main__':
    main()