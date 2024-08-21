# 5 150
# 0 50 10
# 0 50 20
# 50 100 10
# 100 151 10
# 110 140 90

import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

n, d = map(int, input().split())

distances = [INF] * (d+1)
graph = [[] for _ in range(d+1)]

for i in range(d):
    graph[i].append((i+1, 1))

for _ in range(n):
    a, b, c = map(int, input().split())
    if b <= d:
        graph[a].append((b,c))

def dijkstra(s):
    distances[s] = 0
    q = []
    heapq.heappush(q, (0,s))

    while q:
        dist, now = heapq.heappop(q)
        if distances[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distances[i[0]]:
                distances[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(0)
print(distances[-1])