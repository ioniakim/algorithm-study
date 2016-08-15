#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Morse(object):
    def __init__(self):
        self._k = -1

    def morse(self, n, m, k):
        self._k = k
        self._morse(n, m, '')

    def _morse(self, n, m, s):

        if 0 > self._k:
            return

        if 0 == n and 0 == m:
            if 0 == self._k:
                print(s)
            self._k -= 1
            return

        if n > 0:
            self._morse(n-1, m, s + '-')
        if m > 0:
            self._morse(n, m-1, s + 'o')

def morse(n, m, s):

    if n == 0 and m == 0:
        print(s)

    if n > 0 :
        morse(n-1, m, s + '-')
    if m > 0 :
        morse(n, m-1, s + 'o')



def main():
    m = Morse()
    m.morse(100, 100, 10000)

if __name__ == '__main__':
    main()