import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())

graph = [list(map(int, input().split())) for  _ in range(n)]
tree = [[INF] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            tree[i][j] = 1

for k in range(n):
    for s in range(n):
        for e in range(n):
            tree[s][e] = min(tree[s][k]+tree[k][e], tree[s][e])

for i in range(n):
    for j in range(n):
        if tree[i][j] < int(1e9):
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()