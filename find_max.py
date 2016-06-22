#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def find_max(seq):

  max_value = seq[0]
  max_index = 1
  for i, v in enumerate(seq):
    if v > max_value:
      max_value = v
      max_index = i + 1
  return max_index, max_value

def main():
  l = input("numbers(seperated by comma):")

  print(find_max([int(v) for v in l.split(",")]))

if __name__ == '__main__':
  main()