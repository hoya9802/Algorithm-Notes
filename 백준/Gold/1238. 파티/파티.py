import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

n, m, x = map(int, input().split())

to_graph = [[] for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    to_graph[b].append((a,c))

def dijkstra(x,v):
    q = []
    distances = [INF] * (n+1)
    distances[x] = 0
    heapq.heappush(q, (x,0))
    
    while q:
        now, dist = heapq.heappop(q)
        if distances[now] < dist:
            continue
        for i in v[now]:
            cost = dist + i[1]
            if cost < distances[i[0]]:
                distances[i[0]] = cost
                heapq.heappush(q, (i[0], cost))
    
    return distances[1:]

lst = dijkstra(x, graph); to_lst = dijkstra(x, to_graph)

res = 0
for a, b in zip(lst, to_lst):
    if res < a+b:
        res = a+b

print(res)