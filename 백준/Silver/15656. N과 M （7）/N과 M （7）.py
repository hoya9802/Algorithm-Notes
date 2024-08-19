import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = sorted(list(map(int, input().split())))

def dfs(lst):
    if len(lst) == m:
        print(*lst)
        return
    
    for i in range(n):
        dfs(lst+[data[i]])

dfs([])