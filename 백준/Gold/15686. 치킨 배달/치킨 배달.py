import sys
from itertools import combinations as cb
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

home = []; chicken = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            home.append((i,j))
        elif graph[i][j] == 2:
            chicken.append((i,j))
pos_chicken = list(cb(chicken, m))

res = int(1e9)
for pc in pos_chicken:
    temp_sum = 0
    for h in home:
        hx, hy = h
        tmp = int(1e9)
        for c in pc:
            cx, cy = c
            dist = abs(hx-cx) + abs(hy-cy)
            if dist < tmp:
                tmp = dist
        temp_sum += tmp
    if temp_sum < res:
        res = temp_sum
print(res)