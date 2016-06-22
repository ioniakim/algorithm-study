#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

first = True

def reverse(n):
  global first
  if n < 10:
    print(n)
    return

  m = n % 10
  if first and m == 0:
    reverse(n//10)
  else:
    first = False
    print(n % 10, end='')
    reverse(n//10)

def reverse2(n):
  if n < 10:
    return n

  return reverse2(n//10) + (n % 10) * 10 ** int(math.log10(n))

def main():
  n = 100100013240
  reverse(n)
  print(reverse2(n))

if __name__ == '__main__':
  main()