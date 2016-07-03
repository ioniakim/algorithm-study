#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def bino(n, k):
  if n == k or k == 0:
    return 1

  if k == 1:
    return n

  return int((n - k + 1)/k * bino(n, k - 1))


def main():
  print(bino(4, 2))


if __name__ == '__main__':
  main()