#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import wraps

def memo(func):
  cache={}

  @wraps(func)
  def wrap(*args):
    if args not in cache:
      cache[args] = func(*args)
    return cache[args]
  return wrap

def fibo(i):
  if i < 2:
    return 1

  return fibo(i - 1) + fibo(i - 2)


def main():
  fib = memo(fibo)

  print(fib(100))


if __name__ == '__main__':
  main()