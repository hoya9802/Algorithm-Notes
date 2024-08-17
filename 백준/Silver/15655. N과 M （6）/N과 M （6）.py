import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = sorted(list(map(int, input().split())))

def dfs(start, lst):
    if len(lst) == m:
        print(' '.join(map(str, lst)))
        return
    
    for i in range(start, n):
        dfs(i+1, lst+[data[i]])

dfs(0, [])