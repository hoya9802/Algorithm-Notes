import sys
from collections import deque
input = sys.stdin.readline

movement = [(2,-1),(2,1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

def bfs(x, y, ex, ey):
    queue = deque([(x,y,0)])
    visited[x][y] = True
    while queue:
        a, b, c = queue.popleft()
        if a == ex and b == ey:
            return c
        for m in movement:
            nx = a + m[0]; ny = b + m[1]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny] == True:
                continue
            visited[nx][ny] = True
            queue.append((nx, ny, c+1))

for _ in range(int(input())):
    n = int(input())
    visited = [[False] * n for _ in range(n)]
    
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    res = bfs(sx,sy,ex,ey)
    print(res)