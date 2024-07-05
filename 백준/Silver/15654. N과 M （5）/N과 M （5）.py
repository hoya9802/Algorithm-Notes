import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))

s = []
def dfs(n):
    if n == m:
        print(' '.join(map(str, s)))
        return
    for i in sorted(lst):
        if i not in s:
            s.append(i)
            dfs(n+1)
            s.pop()
dfs(0)