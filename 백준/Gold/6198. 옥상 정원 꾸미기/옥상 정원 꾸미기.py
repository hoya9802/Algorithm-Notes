import sys
input = sys.stdin.readline

n = int(input())
bds = [int(input()) for _ in range(n)]

res = 0; stack = []
for cur in bds:
    while stack and stack[-1] <= cur:
        stack.pop()
    stack.append(cur)
    res += len(stack)-1

print(res)