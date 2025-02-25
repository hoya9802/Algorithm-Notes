import sys
input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

def cal(lst):
    temp = 0
    for i in lst:
        for j in lst:
            if i == j:
                continue
            temp += arr[i][j]
    return temp

def dfs(lst, a):
    global res
    if a >= n:
        return
    if len(lst) == n // 2:
        t1 = cal(lst)
        t2 = cal([x for x in range(n) if x not in lst])
        tmp = abs(t1-t2)
        if tmp < res:
            res = tmp
        return

    dfs(lst+[a], a+1)
    dfs(lst, a+1)

res = int(1e9)
dfs([], 0)

print(res)