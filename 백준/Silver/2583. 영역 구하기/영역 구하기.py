import sys
input = sys.stdin.readline

m, n, k = map(int, input().split())
graph = [[0] * n for _ in range(m)]

movement = [(0,1), (0,-1), (1,0), (-1,0)]

def dfs(x,y):
    stack = []
    graph[x][y] = 1
    stack.append((x,y))
    cnt = 1
    while stack:
        x, y = stack.pop()
        for mov in movement:
            nx = x + mov[0]; ny = y + mov[1]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                continue
            graph[nx][ny] = 1
            cnt += 1
            stack.append((nx,ny))
    return cnt

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(y1, y2):
        for y in range(x1, x2):
            graph[x][y] = 1

res = []; ans = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            ans += 1
            res.append(dfs(i,j))
print(ans)
print(*sorted(res))