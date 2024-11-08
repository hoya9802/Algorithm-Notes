import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(set(map(int, input().split())))

def dfs(lst):
    if len(lst) == m:
        print(' '.join(map(str, lst)))
        return
    
    for i in range(len(arr)):
        dfs(lst+[arr[i]])

dfs([])