#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def naive_celeb(G):
    """celebrity brute force algorithm"""
    n = len(G)
    for u in range(n):
        for v in range(n):
            if u == v: continue
            if G[u][v] or not G[v][u]: break
        else:
            return u
    return None


def celeb(G):
    """책의 알고리즘"""
    n = len(G)
    u, v = 0, 1
    for k in range(2, n+1):
        if G[u][v]: u = k
        else: v = k
    c = v if u == n else u
    for k in range(n):
        if c == k: continue
        if G[c][k] or not G[k][c]: break
    else:
        return c
    return None



def celebrity(G):
    """나의 알고리즘"""
    u, v, c = 0, 1, -1
    for k in range(2, len(G)+1):
        if G[u][v]:
            c = v
            u = k
        elif G[v][u]:
            c = u
            v = k
        else:
            u = k

    if c == -1:
        return None

    for i in range(len(G)):
        if i == c: continue
        if G[c][i] or not G[i][c]: break
    else:
        return c

    return None

from random import randrange

def main():
    failed = False
    T = 100

    for t in range(T):
        n = 100
        G = [[randrange(2) for _ in range(n)] for _ in range(n)]
        c = randrange(n)
        for i in range(n):
            G[c][i] = 0
            G[i][c] = 1

        expected = celeb(G)
        actual = celebrity(G)
        naive = naive_celeb(G)
        # print("actual:", actual, "expected:", expected)
        print("celebrity:", c, "actual:", actual, "expected:", expected, "naive:", naive)
        if actual != expected:
            print("Failed")
            break
    else:
        print("Succeeded")



if __name__ == '__main__':
    main()