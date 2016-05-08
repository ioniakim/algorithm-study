'''
너비가 같은 N개의 나무 판자를 붙여 세운 울타리가 있고 각 판자의 높이가 주어질 때 잘라낼 수 있는
직사각형의 최대 크기를 계산하는 프로그램. 판자의 너비는 모두 1이라고 가정

입력:
첫 줄에 테스트 케이스 개수 C (C<=50), 각 테스트 케이스의 첫 줄에는 판자의 수 N(1<=N<=20000)
이 주어짐. 그 다음 줄에는 N개의 정수로부 왼쪽부터 각 판자의 높이가 순서대로 주어짐.
높이는 모두 10,000이하 자연수
'''


def brute_force(fence):
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
      print(brute_force(fence))

if __name__ == '__main__':
 main()