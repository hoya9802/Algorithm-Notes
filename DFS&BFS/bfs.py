from collections import deque

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

def bfs(graph, start_node):
    visited = [False] * len(graph)
    queue = deque() # it is more faster than using List
    queue.append(start_node)
    visited[start_node] = True
    while queue:
        v = queue.popleft()
        print(v, end = " ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(graph, 1)


# 1 2 3 8 7 4 5 6