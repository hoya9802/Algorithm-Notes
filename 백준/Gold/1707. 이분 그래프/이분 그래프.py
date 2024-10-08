import sys
input = sys.stdin.readline

def dfs(x, color):
    stack = [(x, color)]
    while stack:
        now, color = stack.pop()
        if not visited[now]:
            visited[now] = color
            if color == 1: color = 2
            else: color = 1
            for i in graph[now]:
                stack.append((i, color))


for _ in range(int(input())):
    v, e = map(int, input().split())

    visited = [0] * (v+1)
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b); graph[b].append(a)

    for i in range(1,v+1):
        if not visited[i]:
            dfs(i, 1)

    for i in range(1,v+1):
        flag = False
        for j in graph[i]:
            if visited[j] == visited[i]:
                print('NO')
                flag = True
                break
        if flag:
            break
    else:
        print('YES')