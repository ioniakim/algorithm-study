#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' ALGOSPOT Packing
Packing of Dynamic Programming
pack(items) = 지금까지 고른 물건들의 목록이 items에 주어질 때, 남은 용량을 채워 얻을 수 있는 최대의 절박도 합
'''
from collections import namedtuple


class Packing_DP(object):

    def __init__(self):
        self.MAX_SIZE = 100
        self.MAX_CAPACITY = 1000
        self._choosen = [False for _ in range(self.MAX_SIZE)]


    def _init(self, n):
        for i in range(n):
            self._choosen[i] = False


    def _solve(self, item, capacity):

        capacity = capacity - self._items[item].weight
        if capacity < 0:
            return 0

        max_need = 0
        self._choosen[item] = True
        for i in range(self._n):
            if not self._choosen[i]:
                max_need = max(max_need, self._solve(i, capacity))
        self._choosen[item] = False

        return max_need + self._items[item].need


    def solve(self, items, capacity):
        self._n = len(items)
        self._items = items
        self._init(len(items))
        self.count = 0

        self.max_need = 0
        for i in range(self._n):
            self.max_need = max(self.max_need, self._solve(i, capacity))

        return self.max_need


def main():
    Item = namedtuple("Item", ["name", "weight", "need"])

    with open("packing.dat") as f:
        T = int(f.readline())
        p = Packing_DP()
        for case in range(T):
            n, capacity = map(int, f.readline().split())
            items = []
            for i in range(n):
                name, weight, need = f.readline().split()
                items.append(Item(name, int(weight), int(need)))
            p.solve(items, capacity)

            print(p.max_need, p.count)
            # for item in p.choosed:
            #     print(item.name)


if __name__ == "__main__":
    main()