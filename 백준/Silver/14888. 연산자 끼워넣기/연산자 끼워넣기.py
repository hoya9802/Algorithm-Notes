import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_val = int(1e9); max_val = -int(1e9)
def dfs(n, sm, add, sub, mul, div):
    global min_val, max_val
    if n == N:
        min_val = min(sm, min_val)
        max_val = max(sm, max_val)
        return
    
    if add > 0:
        dfs(n+1, sm+lst[n], add-1, sub, mul, div)
    if sub > 0:
        dfs(n+1, sm-lst[n], add, sub-1, mul, div)
    if mul > 0:
        dfs(n+1, sm*lst[n], add, sub, mul-1, div)
    if div > 0:
        dfs(n+1, int(sm/lst[n]), add, sub, mul, div-1)

dfs(1, lst[0], add, sub, mul, div)
print(max_val, min_val, sep='\n')