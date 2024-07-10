import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())
graph = [[] for _ in range(h)]
for d in range(h):
    for _ in range(n):
        temp = list(map(int, input().split()))
        graph[d].append(temp)

movement = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]

q = deque()
for d in range(h):
    for i in range(n):
        for j in range(m):
            if graph[d][i][j] == 1:
                q.append((d,i,j,0))

res = 0
while q:
    d, x, y, t = q.popleft()
    if res < t:
        res = t
    for mov in movement:
        nd = d + mov[0]; nx = x + mov[1]; ny = y + mov[2]
        if nd < 0 or nd >= h or nx < 0 or nx >= n or ny < 0 or ny >= m or graph[nd][nx][ny] != 0:
            continue
        graph[nd][nx][ny] = 1
        q.append((nd,nx,ny,t+1))
Flag = False
for d in range(h):
    for i in range(n):
        for j in range(m):
            if graph[d][i][j] == 0:
                print(-1)
                Flag = True
                break
        if Flag:
            break
    if Flag:
        break
else:
    print(res)