#!/usr/bin/env python3
# -*- coding: utf-8 -*

friends = [[0]*10 for i in range(10)]
paired = [0 for i in range(10)]
n = 0
m = 0

def clear():
  global n
  global friends
  global paired

  for i in range(n):
    for j in range(n):
      friends[i][j] = 0
    paired[i] = 0

def picnic():
  global n
  global friends
  global paired

  not_paired = -1
  for a in range(n):
    if 0 == paired[a]:
      not_paired = 1
      break

  if -1 == not_paired:
    return 1

  # if i > n - 1:
  #   return 0

  count = 0
  paired[not_paired] = 1
  for j in range(not_paired + 1, n):
    if 1 == friends[not_paired][j] and 1 != paired[j]:
      paired[j] = 1
      count += picnic()
      paired[j] = 0

  paired[not_paired] = 0
  return count

def main():
  global friends
  global paired
  global n
  global m

  with open('picnic.dat') as f:
    T = int(f.readline())

    for t in range(T):
      n, m = (int(v) for v in f.readline().split())
      clear()
      pairs = [int(v) for v in f.readline().split()]
      for i in range(0, 2*m, 2):
        friends[pairs[i]][pairs[i+1]] = 1
        friends[pairs[i+1]][pairs[i]] = 1
      print(picnic())

if __name__ == '__main__':
  main()