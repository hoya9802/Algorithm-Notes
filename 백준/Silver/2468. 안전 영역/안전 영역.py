import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
max_val = max(list(map(max, graph)))

def dfs(x,y,limit, visited):
    if x < 0 or x >= n or y < 0 or y >= n or graph[x][y] <= limit or visited[x][y]:
        return 0
    visited[x][y] = True
    dfs(x-1,y,limit,visited)
    dfs(x+1,y,limit,visited)
    dfs(x,y-1,limit,visited)
    dfs(x,y+1,limit,visited)
    return 1

res = 0
for l in range(max_val):
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] or graph[i][j] <= l:
                cnt += dfs(i,j,l,visited)
    if cnt > res:
        res = cnt
print(res)