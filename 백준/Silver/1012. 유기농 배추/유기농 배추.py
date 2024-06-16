import sys
sys.setrecursionlimit(50**3)
input = sys.stdin.readline

def dfs(x, y):
    if x < 0 or x >= len(graph) or y < 0 or y >= len(graph[0]) or graph[x][y] == 0:
        return False
    graph[x][y] = 0
    dfs(x-1, y); dfs(x+1, y); dfs(x, y-1); dfs(x, y+1)
    return True

case = int(input())
for _ in range(case):
    n, m, c = map(int, input().split())
    graph = [[0]*n for _ in range(m)]
    
    for _ in range(c):
        a, b = map(int, input().split())
        graph[b][a] = 1
    res = 0
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if dfs(i,j):
                res += 1
    print(res)