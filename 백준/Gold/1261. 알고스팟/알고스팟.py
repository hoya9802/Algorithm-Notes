import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = []
movement = [(-1,0), (0,1), (1,0), (0,-1)]
for _ in range(m):
    graph.append(list(map(int,input().rstrip())))

def dijkstra(x,y):
    q = []
    distance = [[INF] * (n) for _ in range(m)]
    distance[x][y] = 0
    heapq.heappush(q, (0, x, y))
    while q:
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue
        for i in range(4):
            nx = x + movement[i][0]; ny = y + movement[i][1]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            cost = dist + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))
    return distance[m-1][n-1]

print(dijkstra(0,0))