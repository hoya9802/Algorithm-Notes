import sys
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    temp = list(map(int, input().split()))
    graph.append(temp)

res = int(1e9)

def dfs(cnt, sm, prev, start):
    global res
    if res < sm:
        return

    if cnt == n:
        back_sm = graph[prev][start]
        if back_sm == 0:
            return
        else:
            if res > sm + back_sm:
                res = sm + back_sm
                return
            
    for i in range(n):
        if not visited[i] and graph[prev][i]:
            visited[i] = True
            dfs(cnt+1, sm+graph[prev][i], i, start)
            visited[i] = False

visited = [False] * n
for i in range(n):
    visited[i] = True
    dfs(1,0,i,i)
    visited[i] = False

print(res)