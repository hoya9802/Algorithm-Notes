import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    t, p = map(int, input().split())
    data.append((t,p))

res = 0
def dfs(v, total):
    global res
    if v >= n:
        if res < total:
            res = total
        return
    if v+data[v][0] <= n:
        dfs(v+data[v][0], total+data[v][1])
    dfs(v+1, total)
dfs(0,0)
print(res)