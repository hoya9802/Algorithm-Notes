import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
stack = deque()
for _ in range(N):
    cmd = list(input().split())
    if len(cmd) == 2:
        if cmd[0] == 'push_front':
            stack.appendleft(int(cmd[1]))
        elif cmd[0] == 'push_back':
            stack.append(int(cmd[1]))
    else:
        if cmd[0] == 'pop_front':
            if stack:
                print(stack.popleft())
            else:
                print(-1)
        if cmd[0] == 'pop_back':
            if stack:
                print(stack.pop())
            else:
                print(-1)
        if cmd[0] == 'size':
            print(len(stack))
        if cmd[0] == 'empty':
            if stack:
                print(0)
            else:
                print(1)
        if cmd[0] == 'front':
            if stack:
                print(stack[0])
            else:
                print(-1)
        if cmd[0] == 'back':
            if stack:
                print(stack[-1])
            else:
                print(-1)