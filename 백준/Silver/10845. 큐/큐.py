import sys
from collections import deque
input = sys.stdin.readline

res = deque([])
for _ in range(int(input())):
    cmd = list(map(str, input().split()))
    if len(cmd) > 1:
        res.append(int(cmd[-1]))
    else:
        l = len(res)
        if cmd[-1] == 'pop':
            if l:
                print(res.popleft())
            else:
                print(-1)
        elif cmd[-1] == 'size':
            if l > 0:
                print(l)
            else:
                print(0)
        elif cmd[-1] == 'empty':
            if not res:
                print(1)
            else:
                print(0)
        elif cmd[-1] == 'front':
            if l:
                print(res[0])
            else:
                print(-1)
        else:
            if l:
                print(res[-1])
            else:
                print(-1)    