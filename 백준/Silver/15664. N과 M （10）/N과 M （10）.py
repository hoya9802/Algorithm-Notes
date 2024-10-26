import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))

res = []
def dfs(l, length, s):
    if length == m:
        if l not in res:
            res.append(l)
        return

    for i in range(s,len(lst)):
        dfs(l+[lst[i]], length+1, i+1)

dfs([],0,0)

[print(' '.join(map(str, i))) for i in res]