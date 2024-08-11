import sys
input = sys.stdin.readline

N = int(input())

def dfs(lst):
    if len(lst) == N:
        print(*lst)
        return
    
    for i in range(1,N+1):
        if not visited[i]:
            visited[i] = True
            dfs(lst+[i])
            visited[i] = False

for i in range(1, N+1):
    visited = [False] * (N+1)
    visited[i] = True
    dfs([i])
    visited[i] = False