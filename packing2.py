#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Brute-force algorithm of Packing Defined in Book
The Knapsack problem. 각 짐을 선택하는냐 안하는냐 형태로 알고리즘 구현
"""

from collections import namedtuple
Item = namedtuple("Item", ["name", "weight", "need"])

class Packing(object):
    def __init__(self):
        pass

    def solve(self, items, capacity):
        self._items = items
        self._N = len(items)
        return self._solve(0, capacity)

    def _solve(self, i, capacity):
        if i == self._N:
            return 0

        max_need = self._solve(i + 1, capacity) # in case of not selecting this item

        if capacity >= self._items[i].weight:
            max_need = max(max_need, self._solve(i + 1, capacity - self._items[i].weight) + self._items[i].need)

        return max_need


def main():

    packing = Packing()
    with open("packing.dat") as f:
        T = int(f.readline())
        for _ in range(T):
            n, capacity = map(int, f.readline().split())
            items = []
            for _ in range(n):
                name, weight, need = f.readline().split()
                items.append(Item(name, int(weight), int(need)))

            print(packing.solve(items, capacity))


if __name__ == "__main__":
    main()