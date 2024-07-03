import sys
input = sys.stdin.readline

N, s = map(int, input().split())
lst = list(map(int, input().split()))

ans = 0
def dfs(n, sm, cnt):
    global ans
    if n == N:
        if sm == s and cnt > 0:
            ans += 1
        return
    dfs(n+1, sm+lst[n], cnt+1)
    dfs(n+1, sm, cnt)
dfs(0,0,0)
print(ans)