import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b); graph[b].append(a)

stack = []
def dfs(x):
    cnt = 1
    stack.append(x)

    while stack:
        now = stack.pop()
        if visited[now] == 0:
            visited[now] = cnt
            cnt += 1
            for i in sorted(graph[now], reverse=True):
                stack.append(i)
    return visited[1:]

print(*dfs(r), sep='\n')