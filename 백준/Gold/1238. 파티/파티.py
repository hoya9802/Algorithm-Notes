import sys, heapq
input = sys.stdin.readline
INF = int(1e9)
n, m, t = map(int, input().split())

graph = [[] for _ in range(n+1)]
to_graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    to_graph[b].append((a,c))

def dijkstra(v,gh):
    q = []
    distance = [INF] * (n+1)
    distance[v] = 0
    heapq.heappush(q, (0, v))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in gh[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance[1:]
from_t = dijkstra(t, graph)
to_t = dijkstra(t, to_graph)

res = 0
for a, b in zip(from_t, to_t):
    tmp = a + b
    if tmp > res:
        res = tmp
print(res)