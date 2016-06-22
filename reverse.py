#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def reverse(n):
  if n < 10:
    print(n)
    return

  print(n % 10, end='')
  reverse(n//10)

def main():
  reverse(100)

if __name__ == '__main__':
  main()