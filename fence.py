#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
너비가 같은 N개의 나무 판자를 붙여 세운 울타리가 있고 각 판자의 높이가 주어질 때 잘라낼 수 있는
직사각형의 최대 크기를 계산하는 프로그램. 판자의 너비는 모두 1이라고 가정

입력:
첫 줄에 테스트 케이스 개수 C (C<=50), 각 테스트 케이스의 첫 줄에는 판자의 수 N(1<=N<=20000)
이 주어짐. 그 다음 줄에는 N개의 정수로부 왼쪽부터 각 판자의 높이가 순서대로 주어짐.
높이는 모두 10,000이하 자연수
'''

def divide_conquer(fence, left, right):
  max_rec = 0
  c = right - left
  if c == 1:
    return fence[left]

  mid = left + int(c / 2)
  left_max = divide_conquer(fence, left, mid)
  right_max = divide_conquer(fence, mid, right)

  min_height = min(fence[mid-1], fence[mid])

  lh = mid
  for i in range(mid, left - 1, -1):
    if fence[i] < min_height:
      break
    lh = i

  rh = mid + 2
  for i in range(mid+1, right):
    if fence[i] < min_height:
      break
    rh = i

  return max(left_max, right_max, (rh - lh) * min_height)

def brute_force2(fence):
  """책 예제
  left부터 min_height를 구하면서 최대 직사각형을 찾는 로직
  """
  ret = 0
  N = len(fence)
  for left, h in enumerate(fence):
    min_height = h
    for right in range(left, N):
      min_height = min(min_height, fence[right])
      ret = max(ret, (right - left + 1) * min_height)

  return ret

def brute_force(fence):
  """내가 만든 로직
  left부터 각 판자의 크기에서 가장 큰 직사각형을 찾는 로직
  """
  max_rectangle = -1

  for i, h in enumerate(fence):
    s = 0
    for j in range(i-1, -1, -1):
      if fence[j] < h:
        s = j + 1
        break;
    e = len(fence)
    for j in range(i+1, len(fence)):
      if fence[j] < h:
        e = j
        break;

    count = e - s
    max_rectangle = max(max_rectangle, count * h)

  return max_rectangle

def main():
  with open('fence.dat') as f:
    C = int(f.readline())
    for i in range(C):
      N = int(f.readline())
      fence = [int(h) for h in f.readline().split()]
      print('brute force 1:', brute_force(fence))
      print('brute force 2:', brute_force2(fence))
      max_rec = divide_conquer(fence, 0, len(fence))
      print('divide and conquer:', max_rec)

if __name__ == '__main__':
 main()