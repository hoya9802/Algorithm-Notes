import sys
from collections import deque
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b); graph[b].append(a)

queue = deque([])
def dfs(x):
    cnt = 1
    queue.append(x)

    while queue:
        now = queue.popleft()
        if visited[now] == 0:
            visited[now] = cnt
            cnt += 1
            for i in sorted(graph[now]):
                queue.append(i)
    return visited[1:]

print(*dfs(r), sep='\n')