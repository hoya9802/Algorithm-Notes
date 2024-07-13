import sys
from collections import deque
input = sys.stdin.readline

v = int(input())

graph = [[] for _ in range(v+1)]
for _ in range(v-1):
    a, b = map(int, input().split())
    graph[a].append(b); graph[b].append(a)

parent_node = [0] * (v+1)
visited = [False] * (v+1)
def bfs(v):
    queue = deque([v])
    parent_node[v] = v
    while queue:
        v = queue.popleft()
        visited[v] = True
        for i in graph[v]:
            if not visited[i]:
                parent_node[i] = v
                queue.append(i)
bfs(1)
for i in parent_node[2:]:
    print(i)