import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
sx = sy = 0

pos = [0,0]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            pos[0]=i; pos[1]=j
graph[pos[0]][pos[1]] = 0
movement = [(-1,0), (0,1), (1,0), (0,-1)]
def find_food(pos, limit):
    x, y = pos
    res = []
    visited = [[False] * n for _ in range(n)]
    q = deque([[x, y, 0]])
    while q:
        x,y,time = q.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x + movement[i][0]; ny = y + movement[i][1]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or graph[nx][ny] > limit or visited[nx][ny]:
                continue
            if 0 < graph[nx][ny] < limit:
                res.append([nx,ny,time+1])
            visited[nx][ny] = True
            q.append([nx,ny,time+1])
    res.sort(key=lambda x: (x[2], x[0],x[1]))
    if res:
        return res[0]
    else:
        return False

init_size = 2; eat_count = 0; time = 0
while 1:
    res = find_food(pos, init_size)
    if not res:
        break
    pos = res[:2]; time += res[-1]
    graph[pos[0]][pos[1]] = 0
    eat_count += 1
    if init_size == eat_count:
        init_size += 1; eat_count = 0
print(time)