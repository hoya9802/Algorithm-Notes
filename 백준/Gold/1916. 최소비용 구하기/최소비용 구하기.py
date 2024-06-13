import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
b = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(b):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

distance = [INF] * (n+1)

def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

s, e = map(int, input().split())
dijkstra(s)
print(distance[e])