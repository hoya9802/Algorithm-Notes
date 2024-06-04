import sys
import heapq

input = sys.stdin.readline
N, M, K, x = map(int, input().split())
INF = int(1e9)
distance = [INF] * (N+1)
graph = [[] for _ in range(N+1)]

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
dijkstra(x)
res = [x+1 for x in range(len(distance[1:])) if distance[x+1] == K]
if not res:
    print(-1)
else:
    for i in res:
        print(i)