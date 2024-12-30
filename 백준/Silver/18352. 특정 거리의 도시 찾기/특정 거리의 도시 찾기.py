import sys, heapq
input = sys.stdin.readline

INF = int(1e9)

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append((b))

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + 1
            if cost > K:
                break
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))

dijkstra(X)

res = [str(i+1) for i in range(N) if distance[i+1] == K]
print('\n'.join(res) if res else -1)