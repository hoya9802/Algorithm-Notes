import sys
input = sys.stdin.readline

k = int(input())
s = input().split()
num = [0] * 10
res = []

def dfs(lst, n):
    if len(lst) == k+1:
        res.append(''.join(map(str, lst)))
        return 
    
    start = 0; end = 10
    if s[n] == "<":
        start = lst[-1] + 1
    else:
        end = lst[-1]
    for i in range(start, end):
        if not num[i]:
            num[i] = 1
            dfs(lst+[i], n+1)
            num[i] = 0


for i in range(len(num)):
    num[i] = 1
    tmp = dfs([i],0)
    num[i] = 0

print(res[-1], res[0], sep='\n')