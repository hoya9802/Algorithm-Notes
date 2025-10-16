import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0

def dfs(v):
    global count
    visited = [0] * (n+1)
    stack = [(v, 0)]

    while stack:
        now, layer = stack.pop()
        if visited[now]:
            continue
        visited[now] = 1

        is_leaf = True
        for nxt in graph[now]:
            if not visited[nxt]:
                stack.append((nxt, layer + 1))
                is_leaf = False

        if is_leaf:
            count += layer

dfs(1)
print("Yes" if count % 2 else "No")
