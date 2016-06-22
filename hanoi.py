#!/usr/bin/env python3
# -*- coding: utf-8 -*-

A = [5,4,3,2,1]
B = []
C = []

def hanoi(n, source, target, auxiliary):
  if n > 0:
    hanoi(n - 1, source, auxiliary, target)
    target.append(source.pop())
    print(A, B, C, '###########', sep='\n')
    hanoi(n - 1, auxiliary, target, source)

def main():
  hanoi(len(A), A, B, C)

if __name__ == '__main__':
  main()