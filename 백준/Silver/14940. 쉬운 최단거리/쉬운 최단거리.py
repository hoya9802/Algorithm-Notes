import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
movements = [(-1, 0), (0, 1), (1, 0), (0, -1)]

visited = [[0] * m for _ in range(n)]

sx, sy = 0, 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            graph[i][j] = 0
            sx, sy = i, j

def bfs(x, y):
    q = deque([(x,y)])
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + movements[i][0], y + movements[i][1]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            
            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                visited[nx][ny] = 1
                q.append((nx,ny))

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and visited[i][j] == 0:
                graph[i][j] = -1

bfs(sx, sy)

print('\n'.join(' '.join(map(str, row)) for row in graph))
