import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))

def dfs(v, s):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(v, n):
        s.append(lst[i])
        dfs(i,s)
        s.pop()

dfs(0,[])