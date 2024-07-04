import sys
input = sys.stdin.readline

r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]
visited = [0] * 100
movement = [(-1,0), (0,1), (1,0), (0,-1)]
visited[ord(graph[0][0])] = 1
ans = 1

def dfs(x,y,cnt):
    global ans
    ans = max(ans, cnt)

    for i in range(4):
        nx = x + movement[i][0]; ny = y + movement[i][1]
        if nx < 0 or nx >= r or ny < 0 or ny >= c or visited[ord(graph[nx][ny])] == 1:
            continue
        visited[ord(graph[nx][ny])] = 1
        dfs(nx,ny,cnt+1)
        visited[ord(graph[nx][ny])] = 0
    return
dfs(0,0,1)
print(ans)