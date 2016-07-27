#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def score(seq):
    if all((seq[0] == v for v in seq)):
        return 1

    # 등차수열
    delta = abs(seq[0] - seq[1])
    arithmatic = all((delta == abs(seq[i] - seq[i-1]) for i in range(1, len(seq))))

    # 1씩 증가하거나 감소할 때
    if arithmatic and delta == 1:
        return 2

    # 두 숫자가 번갈아 가며 나타날 때
    if all((seq[i] == seq[i%2] for i in range(len(seq)))):
        return 4

    if arithmatic:
        return 5

    # 그 외
    return 10


def pi(seq):
    if len(seq) <= 5:
        return score(seq)

    point3 = score(seq[:3]) + pi(seq[3:])
    point4 = score(seq[:4]) + pi(seq[4:])
    point5 = score(seq[:5]) + pi(seq[5:])

    return min(point3, point4, point5)

class PI(object):
    """docstring for PI"""
    def __init__(self, seq):
        super(PI, self).__init__()
        self._seq = seq
        self._cache = [-1 for i in range(len(seq))]

    def solve(self):
        return self._solve(0)

    def _solve(self, start):

        if len(self._seq) - start < 5  :
            return self._score(start, len(self._seq))

        if self._cache[start] != -1:
            return self._cache[start]

        point3 = self._score(start, start+3) + self._solve(start+3)
        point4 = self._score(start, start+4) + self._solve(start+4)
        point5 = self._score(start, start+5) + self._solve(start+5)

        self._cache[start] = min(point3, point4, point5)
        return self._cache[start]

    def _score(self, start, end):

        if all((self._seq[start] == self._seq[i] for i in range(start+1, end))):
            return 1

        # 등차수열
        delta = abs(self._seq[start+1] - self._seq[start])
        arithmatic = all((delta == abs(self._seq[i] - self._seq[i-1]) for i in range(start+1, end)))

        # 1씩 증가하거나 감소할 때
        if arithmatic and delta == 1:
            return 2

        # 두 숫자가 번갈아 가며 나타날 때
        if all((self._seq[i] == self._seq[i%2] for i in range(start, end))):
            return 4

        if arithmatic:
            return 5

        # 그 외
        return 10

def main():
    with open('pi.dat') as f:
        t = int(f.readline())
        for i in range(t):
            seq = f.readline().strip()
            num_seq = [int(v) for v in seq]
            print(num_seq)
            print(pi(num_seq))
            # p = PI(num_seq)
            # print(p.solve())


if __name__ == '__main__':
    main()