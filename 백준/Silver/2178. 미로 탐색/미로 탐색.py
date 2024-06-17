import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().rstrip())))

movement = [(-1,0), (0,1), (1,0), (0,-1)]

def bfs(x, y):
    q = deque()
    q.append((x,y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + movement[i][0]; ny = y + movement[i][1]
            if nx < 0 or nx >= len(graph) or ny < 0 or ny >= len(graph[0]) or graph[nx][ny] != 1:
                continue
            graph[nx][ny] = graph[x][y] + 1
            q.append((nx, ny))
    print(graph[n-1][m-1])
bfs(0,0)