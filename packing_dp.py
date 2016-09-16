#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' Packing of Dynamic Programming
pack(items) = 지금까지 고른 물건들의 목록이 items에 주어질 때, 남은 용량을 채워 얻을 수 있는 최대의 절박도 합
'''
from collections import namedtuple


class Packing_DP(object):
    def __init__(self):
        pass

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
            for item in p.choosed:
                print(item.name)

if __name__ == "__main__":
    main()