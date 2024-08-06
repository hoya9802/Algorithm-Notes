import sys, heapq
input = sys.stdin.readline

INF = int(1e9)

n, m, r = map(int, input().split())
t = [0]+list(map(int, input().split()))

graph= [[] for _ in range(n+1)]

for _ in range(r):
    a, b, c = map(int, input().split())
    graph[a].append((b,c)); graph[b].append((a,c))

def dijkstra(x):
    q = []
    distances[x] = 0
    heapq.heappush(q, (x,0))

    while q:
        now, dist = heapq.heappop(q)
        if distances[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distances[i[0]]:
                distances[i[0]] = cost
                heapq.heappush(q, (i[0], cost))

res = 0
for i in range(1,n+1):
    distances = [INF] * (n+1)
    total_item = 0
    dijkstra(i)
    for idx in range(1,n+1):
        if distances[idx] <= m:
            total_item += t[idx]
    if res < total_item:
        res = total_item

print(res)