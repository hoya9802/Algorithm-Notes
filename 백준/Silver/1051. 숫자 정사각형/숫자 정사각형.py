import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[x for x in ','.join(input().split())] for _ in range(n)]

def checker(x, y, l, target):
    if x+l >= n or y+l >=m:
        return 0
    if graph[x+l][y] == graph[x+l][y+l] == target:
        return (l+1) ** 2
    return 0

res = 1
for i in range(n):
    for j in range(m):
        start = graph[i][j]
        length = 0
        for k in range(j+1,m):
            length += 1
            if start == graph[i][k]:
                tmp = checker(i,j,length,start)
                if res < tmp:
                    res = tmp

print(res)