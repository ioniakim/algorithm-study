#!/usr/bin/env python3
# -*- coding: utf-8 -*-


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