#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import namedtuple

class Packing(object):
    def __init__(self):
        self.MAX_SIZE = 100
        self._choosed = [False for _ in range(self.MAX_SIZE)]

    def _init(self):
        for i in range(self.MAX_SIZE):
            self._choosed [i] = False

    def solve(self, items, capacity):
        self._init()
        self._items = items
        self._n = len(items)

        max_need = 0
        for i in range(self._n):
            max_need = max(max_need, self._solve(i, capacity))

        return max_need

    def _solve(self, item, capacity):
        capacity = capacity - self._items[item].weight
        if capacity < 0 :
            return 0

        self._choosed[item] = True
        max_need = 0
        for i in range(self._n):
            if not self._choosed[i]:
                max_need = max(max_need, self._solve(i, capacity))
        self._choosed[item] = False

        return max_need + self._items[item].need


def main():
    Item = namedtuple("Item", ["name", "weight", "need"])
    p = Packing()
    with open('packing.dat') as f:
        T = int(f.readline())
        for case in range(T):
            N, W = map(int, f.readline().split())
            items = []
            for line in range(N):
                name, weight, need = f.readline().split()
                items.append(Item(name, int(weight), int(need)))

            max_need = p.solve(items, W)
            print(max_need)

if __name__ == '__main__':
    main()