import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
graph = []
movement = [(-1,0), (0,1), (1,0), (0,-1)]
for _ in range(n):
    graph.append(list(map(int, input().split())))
q = deque([])
for i in range(len(graph)):
    for j in range(len(graph[0])):
        if graph[i][j] == 1:
            q.append((i,j))
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + movement[i][0]; ny = y + movement[i][1]
        if nx < 0 or nx >= len(graph) or ny < 0 or ny >= len(graph[0]) or graph[nx][ny] != 0:
            continue
        graph[nx][ny] = graph[x][y] + 1
        q.append((nx,ny))
ans = 0; flag = False
for i in range(len(graph)):
    for j in range(len(graph[0])):
        if graph[i][j] > ans:
            ans = graph[i][j]
        if graph[i][j] == 0:
            ans = 0
            flag = True
            break
    if flag:
        break
print(ans-1)