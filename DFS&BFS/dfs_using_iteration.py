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

def dfs(graph, start_node):
    stack = deque()
    visited=[False] * len(graph)
    stack.append(start_node)

    while stack:
        v = stack.pop()
        if not visited[v]:
            print(v, end= " ")
            visited[v] = True
            for i in graph[v][::-1]:
                if not visited[i]:
                    stack.append(i)

dfs(graph, 1)

# output: 1 2 7 6 8 3 4 5