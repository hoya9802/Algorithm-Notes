import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

ans = 0
def dfs(n, sm, tlist):
    global ans
    if n == 4:
        ans = max(ans, sm)
        return
    
    for x, y in tlist:
        for dx, dy in [(-1,0), (0,1), (1,0), (0,-1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny]==0:
                visited[nx][ny] = 1
                dfs(n+1, sm+graph[nx][ny], tlist+[(nx,ny)])
                visited[nx][ny] = 0

for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(1, graph[i][j], [(i,j)])

print(ans)