#!/usr/bin/env python3
# -*- coding: utf-8 -*-

digit="0123456789ABCDEFGHIJ"

def convert(n, k):
  if n < k:
    print(digit[n], end='')
    return

  convert(n//k, k)
  print(digit[n%k], end='')

def main():
  convert(19, 20)
  print()

if __name__ == '__main__':
  main()