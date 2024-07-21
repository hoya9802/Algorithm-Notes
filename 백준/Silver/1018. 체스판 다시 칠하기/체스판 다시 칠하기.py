import sys
input = sys.stdin.readline

def check(x,y):
    bs = 0; ws = 0
    for i in range(x, x+8):
        for j in range(y, y+8):
            if (i+j) % 2 == 0:
                if graph[i][j] != 'B':
                    bs += 1
                if graph[i][j] != 'W':
                    ws += 1
            else:
                if graph[i][j] != 'W':
                    bs += 1
                if graph[i][j] != 'B':
                    ws += 1
    return min(bs, ws)

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]

res = 64
for i in range(n-7):
    for j in range(m-7):
        res = min(check(i,j), res)

print(res)