import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

res = 0
def dfs(lst, pr, visited):
    global res
    if len(lst) == n-1:
        s = sum(lst)
        if res < s:
            res = s
        return
    
    for x in range(n):
        if visited[x] == False:
            visited[x] = True
            dfs(lst+[abs(arr[pr]-arr[x])], x, visited)
            visited[x] = False

for i in range(n):
    visited = [False] * n
    visited[i] = True
    dfs([], i, visited)
    visited[i] = False
print(res)