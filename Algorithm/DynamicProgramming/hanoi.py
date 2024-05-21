# 1번 기둥에 있는 것을 3번 기둥에 하노이 탑을 이용해서 넣는 방법
import math

n = int(input())

def hanoi(n, start, target, temp): # start: 시작 기둥, target: 타겟 기둥, temp: 보조 기둥
    if n == 1:
        print(start, '->', target)
    else:
        hanoi(n-1, start, temp, target)
        print(start, '->', target)
        hanoi(n-1, temp, target, start)
hanoi(n, 1, 3, 2)
print('총 횟수 :', 2**n-1)
