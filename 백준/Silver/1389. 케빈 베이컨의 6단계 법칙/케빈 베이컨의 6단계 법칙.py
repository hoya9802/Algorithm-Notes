import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

def bfs(x):
    visited = [-1] * (n+1)
    visited[x] = 0
    q = deque([[x, 0]])
    while q:
        s, c = q.popleft()
        c += 1
        for i in graph[s]:
            if visited[i] == -1:
                visited[i] = c
                q.append([i, c])
    return sum(visited[1:])

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b); graph[b].append(a)

min_val = 1e9; res = 0
for i in range(1,n+1):
    temp = bfs(i)
    if min_val > temp:
        min_val = temp
        res = i

print(res)