#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def merge(s1, s2):
    failed = False
    res = s1
    for i in range(len(s1)):
        failed = False
        for j in range(len(s2)):
            if i + j >= len(s1):
                return s1 + s2[j:]
            if s1[i + j] != s2[j] :
                failed = True
                break
        if not failed :
            return res
    return s1 + s2


def restore(seq):
    if len(seq) == 1:
        return seq[0]

    res = None
    for e in seq:
        s = merge(e, restore([o for o in seq if o != e]))
        res = s if res == None or len(s) < len(res)  else res
    return res


def main():
    with open('restore.txt') as f:
        T = int(f.readline())
        for i in range(T):
            c = int(f.readline())
            seq = []
            for _ in range(c):
                seq.append(f.readline().strip())
            print(restore(seq))




if __name__ == '__main__':
    main()