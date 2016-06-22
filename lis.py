#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from itertools import combinations

def naive_lis(seq):
  for length in range(len(seq), 0, -1):
    for sub in combinations(seq, length):
      if list(sub) == sorted(sub):
        return sub

def main():
  help(combinations)
  l = [3, 1, 0, 2, 4]
  print(naive_lis(l))

if __name__ == '__main__':
  main()