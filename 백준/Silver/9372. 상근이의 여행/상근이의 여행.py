import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b); graph[b].append(a)
    res = 0
    visited = [False] * (n+1)
    def dfs(v):
        global res
        stack = deque([v])
        while stack:
            now = stack.pop()
            if not visited[now]:
                visited[now] = True
                res += 1
                for i in graph[now]:
                    if not visited[i]:
                        stack.append(i)
    dfs(1)
    print(res-1)