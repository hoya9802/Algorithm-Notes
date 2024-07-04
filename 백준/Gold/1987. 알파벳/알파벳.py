import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]
movement = [(-1,0), (0,1), (1,0), (0,-1)]

def bfs():
    ans = 1
    q = deque([(0,0,graph[0][0])])
    visited = [[set() for _ in range(c)] for _ in range(r)]
    visited[0][0].add(graph[0][0])
    while q:
        x, y, v = q.popleft()
        ans = max(len(v), ans)
        for i in range(4):
            nx = x + movement[i][0]; ny = y + movement[i][1]
            if nx < 0 or nx >= r or ny < 0 or ny >= c or graph[nx][ny] in v:
                continue
            if v + graph[nx][ny] in visited[nx][ny]:
                continue
            q.append((nx,ny,v+graph[nx][ny]))
            visited[nx][ny].add((v+graph[nx][ny]))
    return ans

print(bfs())