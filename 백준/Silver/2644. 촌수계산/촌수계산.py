import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
x, y = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b); graph[b].append(a)

q = deque([])
visited = [0] * (n+1)

res = -1
def bfs(s):
    global res
    visited[s] = 1
    q.append((s, res+1))

    while q:
        now, cost = q.popleft()
        if now == y:
            res = cost
            break
        for i in graph[now]:
            if not visited[i]:
                q.append((i, cost+1))
                visited[i] = 1

    return res

print(bfs(x))