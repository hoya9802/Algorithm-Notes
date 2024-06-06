import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    cmd = input()
    l = int(input())
    lst = input()
    if cmd.count('D') > l:
        print('error')
        continue
    lst = deque(list(lst[1:-2].split(',')))
    flag = 0
    for c in cmd:
        if c == 'R':
            flag += 1
        if c == 'D':
            if flag % 2 == 0:
                lst.popleft()
            else:
                lst.pop()
    else:
        if flag % 2 == 0:
            print('['+','.join(lst)+']')
        else:
            lst.reverse()
            print('['+','.join(lst)+']')