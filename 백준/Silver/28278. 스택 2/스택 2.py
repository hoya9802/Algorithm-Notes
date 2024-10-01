import sys
input = sys.stdin.readline

stack = []
for _ in range(int(input())):
    cmd = tuple(map(int, input().split()))
    l = len(cmd)
    if l > 1:
        stack.append(cmd[-1])
        continue
    if cmd[0] == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    if cmd[0] == 3:
        print(len(stack))

    if cmd[0] == 4:
        if not stack:
            print(1)
        else:
            print(0)
    
    if cmd[0] == 5:
        if stack:
            print(stack[-1])
        else:
            print(-1)