# time complexity: O(N^3)
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for i in range(n + 1):
    for j in range(n + 1):
        if i == j:
            graph[i][j] = 0

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] != INF:
            print(graph[i][j], end = " ")
        else:
            print('INFINITY')
    print()

"""
input:
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
------
output:
0 4 8 6 
3 0 7 9 
5 9 0 4 
7 11 2 0 
"""