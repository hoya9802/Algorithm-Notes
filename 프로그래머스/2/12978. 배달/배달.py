# solve 6

def solution(N, road, K):
    INF = int(1e9)
    graph = [[INF] * (N+1) for _ in range(N+1)]
    for r in road:
        a, b, c = r
        graph[a][b] = min(graph[a][b],c); graph[b][a] = min(graph[b][a],c)
    for i in range(N+1):
        for j in range(N+1):
            if i == j:
                graph[i][j] = 0
    for k in range(1, N+1):
        for x in range(1, N+1):
            for y in range(1, N+1):
                graph[x][y] = min(graph[x][k] + graph[k][y], graph[x][y])
    return sum(1 for x in graph[1] if x <= K)