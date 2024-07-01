import sys
input = sys.stdin.readline

n = int(input())
v1 = [0] * n
v2 = [0] * (2*n)
v3 = [0] * (2*n)

cnt = 0
def dfs(v):
    global cnt
    if v == n:
        cnt += 1
        return
    for i in range(n):
        if v1[i] == v2[i+v] == v3[i-v] == 0:
            v1[i] = v2[i+v] = v3[i-v] = 1
            dfs(v+1)
            v1[i] = v2[i+v] = v3[i-v] = 0

dfs(0)
print(cnt)