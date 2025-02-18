import sys
input = sys.stdin.readline

a, b = map(int, input().split())
res = -1
def dfs(x, cnt):
    global res
    if x > b:
        return
    if x == b:
        res = cnt + 1
        return
    dfs(x*2, cnt+1)
    dfs(int(str(x)+"1"), cnt+1)

dfs(a, 0)
print(res)