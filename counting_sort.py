#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict


def counting_sort(A, key=lambda x: x):
    D = defaultdict(list)

    for i in A:
        D[key(i)].append(i)

    ret = []
    for k in range(min(D), max(D) + 1):
        ret.extend(D[k])
    return ret

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

def counting_sort3(arr, key=ord, vrange = 256):
    """ Counting sort in geeksforgeeks
        Input is ASCII code set
    """
    # count array to store count of individual
    # characters and initialize count array as 0
    count = [0 for _ in range(vrange)]

    # Output array that will have sorted arr
    output = [None for _ in arr]

    # Store count of each character
    for c in arr:
        count[key(c)] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this character in output array
    for i in range(1, vrange):
        count[i] += count[i-1]

    # Build the output char array
    for c in arr:
        count[key(c)] -= 1
        output[count[key(c)]] = c

    return output


def main():
    a = [10, 4, 3, 10, 3, 2, 5, 8, 4, 6]
    print(counting_sort(a))
    print(counting_sort2(a))

    c = chr(255) + "flksfjljwlaejwzkj" + chr(0)
    print(counting_sort3(c))


if __name__ == '__main__':
    main()