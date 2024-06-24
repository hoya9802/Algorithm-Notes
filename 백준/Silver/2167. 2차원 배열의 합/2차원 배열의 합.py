import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0]*(m+1)]
for _ in range(n):
    graph.append([0]+list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, m+1):
        graph[i][j] = graph[i][j-1] + graph[i-1][j] - graph[i-1][j-1] + graph[i][j]

for _ in range(int(input())):
    sx, sy, ex, ey = map(int, input().split())
    print(graph[ex][ey] - graph[ex][sy-1] - graph[sx-1][ey] + graph[sx-1][sy-1])