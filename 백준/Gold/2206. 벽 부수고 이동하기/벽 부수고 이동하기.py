import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

movement = [(-1,0), (0,1), (1,0), (0,-1)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

graph = []
for _ in range(n):
    row = input().rstrip()
    graph.append(list(map(int, row)))

def bfs():
    q = deque([[0,0,0]])
    visited[0][0][0] = 1

    while q:
        x, y, w = q.popleft()

        if x == n-1 and y == m-1:
            print(visited[x][y][w])
            return
        
        for mov in range(4):
            nx = x + movement[mov][0]; ny = y + movement[mov][1]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0 and visited[nx][ny][w] == 0:
                visited[nx][ny][w] = visited[x][y][w] + 1
                q.append([nx,ny,w])
            
            elif graph[nx][ny] == 1 and w == 0:
                visited[nx][ny][1] = visited[x][y][w] + 1
                q.append([nx,ny,1])
    else:
        print(-1)

bfs()