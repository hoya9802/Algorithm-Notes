import sys
input = sys.stdin.readline

L, C = map(int, input().split())
data = sorted(list(input().split()))

def check(x):
    cnt = 0
    for i in x:
        if i in ['a','i','o','u','e']:
            cnt += 1
    if 1 <= cnt <= L-2:
        return True
    return False

def dfs(n, s):
    if len(s) > L:
        return
    if n == C:
        if check(s) and len(s) == L:
            print(''.join(s))
        return
    dfs(n+1, s+[data[n]])
    dfs(n+1, s)

dfs(0,[])