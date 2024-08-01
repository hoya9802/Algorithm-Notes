import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(x, y):
    if x<0 or x>=h or y<0 or y>=w:
        return
    if graph[x][y] == 0:
        return
    graph[x][y] = 0
    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)
    dfs(x-1,y-1)
    dfs(x-1,y+1)
    dfs(x+1,y-1)
    dfs(x+1,y+1)

while 1:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]
    
    land = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                land += 1
                dfs(i, j)

    print(land)