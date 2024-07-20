import sys
input = sys.stdin.readline

def check_row(x, n):
    for i in range(9):
        if graph[x][i] == n:
            return False
    else:
        return True

def check_column(y, n):
    for i in range(9):
        if graph[i][y] == n:
            return False
    else:
        return True

def check_box(x, y, n):
    for i in range((x//3)*3,(x//3)*3+3):
        for j in range((y//3)*3,(y//3)*3+3):
            if graph[i][j] == n:
                return False
    else:
        return True

def dfs(v):
    if v == len(blank):
        for i in range(9):
            print(' '.join(map(str,graph[i])))
        exit()
    
    x = blank[v][0]; y = blank[v][1]
    for i in range(1,10):
        if check_row(x, i) and check_column(y, i) and check_box(x,y,i):
            graph[x][y] = i
            dfs(v+1)
            graph[x][y] = 0

graph = [list(map(int, input().split())) for _ in range(9)]
blank = []
for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            blank.append((i,j))

dfs(0)