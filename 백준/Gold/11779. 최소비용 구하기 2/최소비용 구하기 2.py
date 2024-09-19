import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

n = int(input()); m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
s, e = map(int, input().split())

distances = [[INF, [i]] for i in range(n + 1)]
def dijkstra(x):
    distances[x][0] = 0
    q = []
    heapq.heappush(q, (0, x))
    while q:
        dist, now = heapq.heappop(q)
        if distances[now][0] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distances[i[0]][0]:
                distances[i[0]][0] = cost
                distances[i[0]][1] = distances[now][1] + [i[0]]
                heapq.heappush(q, (cost, i[0]))

dijkstra(s)
print(distances[e][0], len(distances[e][1]), sep='\n')
print(*distances[e][1])