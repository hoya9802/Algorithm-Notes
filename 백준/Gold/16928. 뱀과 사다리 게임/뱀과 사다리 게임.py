import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(101)]
visited = [False] * (101)

for _ in range(n+m):
    a, b = map(int, input().split())
    graph[a].append(b)

def check(x):
    if not graph[x]:
        return x
    return check(graph[x][0])

stack = deque([])
def dfs(x):
    stack.append((x, 0))

    while stack:
        now, cnt = stack.popleft()
        if now == 100:
            return cnt
        if graph[now]:
            now = check(now)
        for i in range(1, 7):
            if (now + i) <= 100 and not visited[now + i]:
                visited[now + i] = True
                stack.append((now + i, cnt+1))

print(dfs(1))