import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    cmd = list(input().split())
    if len(cmd) >= 2:
        stack.append(cmd[1])
    else:
        if cmd[0] == 'pop':
            if stack:
                v = stack.pop()
                print(v)
            else:
                print(-1)
        if cmd[0] == 'size':
            print(len(stack))
        if cmd[0] == 'empty':
            if not stack:
                print(1)
            else:
                print(0)
        if cmd[0] == 'top':
            if stack:
                print(stack[-1])
            else:
                print(-1)