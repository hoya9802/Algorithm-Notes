import sys
input = sys.stdin.readline

n = int(input())
stack = []
for _ in range(n):
    cmd = int(input())
    if cmd == 0:
        stack.pop()
        continue
    stack.append(cmd)
if not stack:
    print(0)
else:
    print(sum(stack))