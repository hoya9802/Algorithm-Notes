import sys, heapq
input = sys.stdin.readline

INF = int(1e9)
movement = [(-1,0), (0,1), (1,0), (0,-1)]
i = 1
while 1:
    n = int(input())
    if n == 0:
        break
    graph = []
    distances = [[INF] * n for _ in range(n)]
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    def dijkstra(x,y):
        q = []
        distances[x][y] = graph[x][y]
        heapq.heappush(q, (graph[x][y], x, y))

        while q:
            dist, x, y = heapq.heappop(q)
            if x == n-1 and y == n-1:
                break
            if distances[x][y] < dist:
                continue
            for i in range(4):
                nx = x + movement[i][0]; ny = y + movement[i][-1]
                if -1 < nx < n and -1 < ny < n and dist + graph[nx][ny] < distances[nx][ny]:
                    distances[nx][ny] = dist + graph[nx][ny]
                    heapq.heappush(q, (distances[nx][ny], nx, ny))
    dijkstra(0,0)
    print(f'Problem {i}: {distances[n-1][n-1]}')
    i += 1