def dfs(graph, visited, node):
    stack = [node]
    while stack:
        v = stack.pop()
        visited[v] = 1
        for i in graph[v]:
            if visited[i] == 0:
                stack.append(i)

def solution(n, computers):
    graph = [[] for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if computers[i][j] == 1:
                graph[i+1].append(j+1)
                
    visited = [0] * (n+1)
    
    answer = 0
    for i in range(n):
        if visited[i+1] == 0:
            answer += 1
            dfs(graph, visited, i+1)
    
    return answer