import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]

res = 100**2
for i in range(n-7):
    for j in range(m-7):
        w_case = 0; b_case = 0
        for x in range(i,i+8):
            for y in range(j,j+8):
                if (x+y) % 2 == 0:
                    if graph[x][y] != 'W':
                        w_case += 1
                    if graph[x][y] != 'B':
                        b_case += 1
                else:
                    if graph[x][y] != 'B':
                        w_case += 1
                    if graph[x][y] != 'W':
                        b_case += 1
        tmp = min(w_case, b_case)
        if res > tmp:
            res = tmp

print(res)