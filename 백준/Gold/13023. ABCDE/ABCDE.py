import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b); graph[b].append(a)

def dfs(lst):
    global res
    if len(lst) == 5:
        res = 1
        return
    
    for i in graph[lst[-1]]:
        if i not in lst:
            dfs(lst+[i])

res = 0
for i in range(n):
    dfs([i])
    if res == 1:
        break

print(res)