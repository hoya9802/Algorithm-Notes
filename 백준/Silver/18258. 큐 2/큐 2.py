import sys
from collections import deque
input = sys.stdin.readline

res = deque([])
n = int(input())
for i in range(n):
    cmd = input().split()

    if cmd[0] == 'push':
        res.append(cmd[-1])
        continue
    if cmd[0] == 'pop':
        if not res:
            print(-1)
            continue
        print(res.popleft())
    if cmd[0] == 'size':
        print(len(res))
    if cmd[0] == 'empty':
        if not res:
            print(1)
            continue
        print(0)
    if cmd[0] == 'front':
        if not res:
            print(-1)
            continue
        print(res[0])
    if cmd[0] == 'back':
        if not res:
            print(-1)
            continue
        print(res[-1])