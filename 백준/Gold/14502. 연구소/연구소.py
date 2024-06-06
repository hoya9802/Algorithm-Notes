import sys, copy
from collections import deque
from itertools import combinations as cb
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
e_idx = []
virus = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            e_idx.append((i,j))
        if graph[i][j] == 2:
            virus.append((i,j))
pos_bar = list(cb(e_idx, 3))
def bfs(g, x, y):
    q = deque([(x,y)])
    movement = [(-1,0), (0,1), (1,0), (0,-1)]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + movement[i][0]; ny = y + movement[i][1]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if g[nx][ny] == 1 or g[nx][ny] == 2:
                continue
            g[nx][ny] = 2
            q.append((nx, ny))

max_val = 0
for i in range(len(pos_bar)):
    c_graph = copy.deepcopy(graph)
    temp = 0
    for b in pos_bar[i]:
        x, y = b
        c_graph[x][y] = 1
    for v in virus:
        x, y = v
        bfs(c_graph, x, y)
    for j in range(n):
        for k in range(m):
            if c_graph[j][k] == 0:
                temp += 1
    if temp > max_val:
        max_val = temp
print(max_val)