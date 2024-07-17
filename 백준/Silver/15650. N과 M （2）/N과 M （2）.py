import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def dfs(s, start):
    if len(s) == m:
        print(' '.join(map(str, s)))
    for i in range(start, n+1):
        if i not in s:
            s.append(i)
            dfs(s, i+1)
            s.pop()

dfs([], 1)