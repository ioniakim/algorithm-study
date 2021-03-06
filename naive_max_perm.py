#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Finding a Maximum Permutation
Eight persons with very particular tastes have bought tickets to movies. Some of them are happy with their seats, but most of them are not, adn after standing in line, they're getting a bit grumpy. Let's say each of them has favorite seat, and you want to fidn a way to let them switch seats to make as many people as possible happy with the result. However, because they are all rather grumpy, all of them refuse to move to another seat if they can't get their favorite.
"""

def naive_max_perm(M, A=None):
    if not A:
        A = set(range(len(M)))  # pointing
    if len(A) == 1:
        return A
    B = set(M[i] for i in A) # pointed
    C = A - B
    if C:
        A.remove(C.pop())
        return naive_max_perm(M, A)
    return A


def main():
    M = [2, 2, 0, 5, 3, 5, 7, 4]
    print(naive_max_perm(M))


if __name__ == '__main__':
    main()