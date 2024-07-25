import sys
input = sys.stdin.readline

n = int(input())

graph = [list(map(int, input().split())) for  _ in range(n)]

for k in range(n):
    for s in range(n):
        for e in range(n):
            if graph[s][k] and graph[k][e]:
                graph[s][e] = 1

for i in range(n):
    for j in range(n):
        print(graph[i][j], end= " ")
    print()