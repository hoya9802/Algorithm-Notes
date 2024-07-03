import sys
input = sys.stdin.readline

while 1:
    t = list(map(int, input().split()))
    if len(t) == 1:
        break
    N = t[0]; tc = t[1:]
    
    def dfs(n, s):
        if n == N:
            if len(s) == 6:
                print(' '.join(map(str, s)))
            return
        dfs(n+1, s+[tc[n]])
        dfs(n+1, s)
    dfs(0,[])
    print()