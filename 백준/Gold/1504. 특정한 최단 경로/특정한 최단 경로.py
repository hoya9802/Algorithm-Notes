import sys, heapq
input = sys.stdin.readline

INF = int(1e9)

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b,c)); graph[b].append((a,c))

def dijkstra(v, target):
    distance = [INF] * (n+1)
    q = []
    heapq.heappush(q, (0, v))
    distance[v] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance[target]

t1, t2 = map(int, input().split())

res = dijkstra(1, t1)+dijkstra(t1, t2)+dijkstra(t2, n)
res2 = dijkstra(1, t2)+dijkstra(t2, t1)+dijkstra(t1, n)
ans = min(res, res2)
if ans >= INF:
    print(-1)
else:
    print(ans)