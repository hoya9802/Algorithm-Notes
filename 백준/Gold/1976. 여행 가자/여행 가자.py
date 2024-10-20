import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x > y:
        parents[x] = y
    else:
        parents[y] = x

n = int(input())
m = int(input())
parents = [x for x in range(n+1)]

for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] == 1:
            union(i+1, j+1)

ans = list(map(int, input().split()))
check = find(ans[0])

for i in ans[1:]:
    if check != find(i):
        print('NO')
        break
else:
    print('YES')
