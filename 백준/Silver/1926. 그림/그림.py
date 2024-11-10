import sys
input = sys.stdin.readline

def dfs(x,y):
    stack = [(x,y)]
    graph[x][y] = 0
    res = 1
    while stack:
        x, y = stack.pop()
        for i in range(len(movement)):
            nx = x + movement[i][0]; ny = y + movement[i][1]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                res += 1
                graph[nx][ny] = 0
                stack.append((nx, ny))
    return res

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

movement = [(-1,0), (1,0), (0,-1), (0,1)]

ans = [0,0]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            tmp = dfs(i,j)
            ans[0] += 1
            if ans[1] < tmp:
                ans[1] = tmp

print(*ans, sep='\n')