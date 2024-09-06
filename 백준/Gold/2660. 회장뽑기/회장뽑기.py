import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
graph = [[] for _ in range(n+1)]

while 1:
    a, b = map(int, input().split())
    if a == b == -1:
        break

    graph[a].append((b,1))
    graph[b].append((a,1))

def dijkstra(x):
    distance = [INF] * (n+1)
    q = []
    distance[x] = 0
    heapq.heappush(q, (0, x))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return max(distance[1:])

tmp = [0] * (n+1)
for i in range(n):
    tmp[i+1] = dijkstra(i+1)

min_val = min(tmp[1:])
res = []; count = 0
for i in range(1,n+1):
    if min_val == tmp[i]:
        count += 1
        res.append(i)
print(min_val, count)
print(*sorted(res))