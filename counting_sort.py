#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict

def counting_sort2(A, key=lambda x: x):
    """ key에 대해서 counting만 함. key와 value가 같은 경우에만 사용 가능
    메모리를 조금 아낄 수 있음.
    """
    D = defaultdict(int)

    for i in A:
        D[key(i)] += 1

    ret = []
    for k in range(min(D), max(D) + 1):
        for c in range(D[k]):
            ret.append(k)
    return ret

def counting_sort(A, key=lambda x: x):
    D = defaultdict(list)

    for i in A:
        D[key(i)].append(i)

    ret = []
    for k in range(min(D), max(D) + 1):
        ret.extend(D[k])
    return ret


def main():
    a = [10, 4, 3, 10, 3, 2, 5, 8, 4, 6]
    print(counting_sort(a))
    print(counting_sort2(a))


if __name__ == '__main__':
    main()