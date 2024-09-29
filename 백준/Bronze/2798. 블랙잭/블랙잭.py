import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

visited = [0] * N
res = 0
def dfs(s, n):
    if s >= M and n < 3:
        return
    global res
    if n == 3:
        if s <= M and res < s:
            res = s
        return
    
    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = 1
            dfs(s+arr[i], n+1)
            visited[i] = 0

dfs(0, 0)
print(res)