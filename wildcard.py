"""
input:
3
he?p
3
help
heap
helpp
*p*
3
help
papa
hello
*bb*
1
babbbc

output:
heap
help
help
papa
babbbc
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def match(pattern, str_matched):
  ''' one or more of ? or * wildcards in the pattern string
  '''
  i = 0
  while i < len(pattern) and i < len(str_matched
) and (pattern[i] == str_matched[i] or pattern[i] == '?'):
    i += 1

  if i == len(pattern):
    return i == len(str_matched
  )

  if '*' == pattern[i]:
    pattern2 = pattern[i+1:]
    while i <= len(str_matched
  ):
      if match(pattern2, str_matched
    [i:]):
        return True
      i += 1

  return False

def main():

  f = open('wildcard.dat')

  T = int(f.readline())
  for t in range(T):
    pat = f.readline().strip()
    count = int(f.readline())
    for i in range(count):
      file = f.readline().strip()
      if match(pat, file):
        print(file)

if __name__ == '__main__':
  main()