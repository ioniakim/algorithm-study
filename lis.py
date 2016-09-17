#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Longest Increasing Subsequence

f(seq) = 0  if len(seq) == 0
f(seq) = 1 if len(seq) == 1
f(seq) = max(f(seq[i:]) for 1 < i < len(seq))
'''


from itertools import combinations

def naive_lis(seq):
  for length in range(len(seq), 0, -1):
    for sub in combinations(seq, length):
      if list(sub) == sorted(sub):
        return sub


def lis(seq):
  res = 0

  if len(seq) == 0 :
    return res

  for i in range(len(seq)):
    subseq = []
    res = max(res, 1 + lis([s for s in seq[i+1:] if s > seq[i] ] ) )

    # for j in range(i + 1, len(seq)):
    #   if seq[i] < seq[j]:
    #     subseq += seq[j]
    # res = max(res, 1 + lis(subseq))

  return res

class Lis2(object):
  """docstring for Lis2"""

  def __init__(self):
    super(Lis2, self).__init__()
    self._MAX = 101
    self.cache = [-1 for i in range(self._MAX)]

  def solve(self, seq):
    self.seq = seq
    for i in range(len(seq)):
      self.cache[i] = -1

    # return self._solve(-1)
    res = 0
    for i in range(len(seq)):
      res = max(res, self._solve(i))

    return res

  def _solve(self, i):
    if (self.cache[i] != -1):
      return self.cache[i]

    self.cache[i] = 1

    for j in range(i+1, len(self.seq)):
      if self.seq[i] < self.seq[j]:
        self.cache[i] = max(self.cache[i], self._solve(j) +1)

    return self.cache[i]



def main():
  l = [3, 1, 0, 2, 4]
  print(naive_lis(l))
  lis2 = Lis2()
  print(lis2.solve(l))

if __name__ == '__main__':
  main()
