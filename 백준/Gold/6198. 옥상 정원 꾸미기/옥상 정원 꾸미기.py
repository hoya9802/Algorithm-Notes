import sys

input = sys.stdin.readline

bds = [int(input()) for _ in range(int(input()))]

stack = []; res = 0

for c in bds:
    while stack and stack[-1] <= c:
        stack.pop()
    stack.append(c)
    res += len(stack) - 1

print(res)