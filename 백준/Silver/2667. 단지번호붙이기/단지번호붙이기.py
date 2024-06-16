import sys
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

def dfs(x, y):
    if x < 0 or x >= len(graph) or y < 0 or y >= len(graph[0]) or graph[x][y] == 0:
        return 0
    temp = graph[x][y]
    graph[x][y] = 0
    return temp + dfs(x-1,y) + dfs(x+1,y) + dfs(x,y-1) + dfs(x,y+1)

res = []
for i in range(len(graph)):
    for j in range(len(graph[0])):
        tmp = dfs(i,j)
        if tmp > 0:
            res.append(tmp)
print(len(res))
for i in sorted(res):
    print(i)