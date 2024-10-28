import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
rlst = lst[::-1]

up = [1] * n; down = [1]*n
for i in range(n):
    for j in range(i):
        if lst[i] > lst[j]:
            up[i] = max(up[i], up[j]+1)
        if rlst[i] > rlst[j]:
            down[i] = max(down[i], down [j]+1)

res = 0
for a, b in zip(up, down[::-1]):
    if res < a+b-1:
        res = a+b-1

print(res)