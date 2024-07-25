import sys
input = sys.stdin.readline

def dfs(p, visited):
    for q in arr[p]:
        if not visited[q]:
            visited[q] = 1
            dfs(q, visited)
    return

N = int(input())
arr = [list() for i in range(N)]

for i in range(N):
    m = list(map(int, input().split()))
    for j in range(N):
        if m[j]: arr[i].append(j)
ans = []

for i in range(N):
    visited = [0] * N
    dfs(i, visited)
    ans.append(' '.join(list(map(str, visited))))

print("\n".join(ans))