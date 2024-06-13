from itertools import chain

def solution(n):
    movement = [(1,0), (0,1), (-1,-1)]
    graph = [[0] * n for n in range(1,n+1)]
    x, y = -1, 0; f = 1
    for i in range(n):
        for j in range(i, n):
            x += movement[i%3][0]; y += movement[i%3][1]
            graph[x][y] = f
            f += 1
    return list(chain(*graph))