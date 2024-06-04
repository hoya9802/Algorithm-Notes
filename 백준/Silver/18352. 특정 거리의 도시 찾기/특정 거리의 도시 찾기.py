import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e9)
N, M, K, x = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [INF] * (N+1)

def bfs(x):
    visited = [False] * (N+1)
    dist = 0
    q = deque([[x, dist]])
    while q:
        v, dist = q.popleft()
        if not visited[v]:
            visited[v] = True
            distance[v] = dist
            if dist > K:
                break
            for i in graph[v]:
                dist = distance[v] + 1
                q.append([i, dist])

bfs(x)
check = False
for i in range(len(distance[1:])):
    if distance[i+1] == K:
        print(i+1)
        check = True
if not check:
    print(-1)