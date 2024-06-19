import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
res = [-1] * n
stack = []
for i in range(len(lst)-1, -1, -1):
    while stack and lst[i] >= stack[-1]:
        stack.pop()
    if stack:
        res[i] = stack[-1]
    stack.append(lst[i])
for i in res:
    print(i, end=" ")