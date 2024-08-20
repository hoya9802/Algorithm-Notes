import sys
input = sys.stdin.readline

n, m = map(int, input().split())

data = sorted(list(set(map(int, input().split()))))
def dfs(lst,x):
    if len(lst) == m:
        print(*lst)
        return 
    for i in range(x,len(data)):
        dfs(lst+[data[i]],i)

dfs([],0)