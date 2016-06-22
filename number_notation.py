#!/usr/bin/env python3
# -*- coding: utf-8 -*-

D = "0123456789ABCDEFGHIJ"

def convert(n, k):
  if n < k :
    print(D[n], end='')
    return

  convert(n // k, k)

  mod = n % k
  print(D[mod], end='')



def main():
  convert(134, 20)
  print()


if __name__ == '__main__':
  main()