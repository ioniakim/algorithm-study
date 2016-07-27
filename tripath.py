#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class TriPath(object):
  """docstring for TriPath
"""
  def __init__(self, n):
    super(TriPath
    , self).__init__()
    self.n = n
    self.tripath = [[-1 for _ in range (i)] for i in range(1, self.n+1)]

  def init(self):
    for l in self.tripath:
      for i in range(len(l)):
        l[i] = -1



def count(y, x):
  pass

def main():
  n = 10
  counter = TriPath(n)
  print(list(map(len, counter.tripath)))
  counter.init()


if __name__ == '__main__':
  main()