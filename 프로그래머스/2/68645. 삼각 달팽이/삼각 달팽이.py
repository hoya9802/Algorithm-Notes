from itertools import chain

def solution(n):
    answer = [[0] * (i+1) for i in range(n)]
    movements = [(1,0), (0,1), (-1,-1)]
    x, y, p = -1, 0, 1
    for i in range(n):
        for _ in range(i,n):
            dx, dy = movements[i%3]
            x = x + dx; y = y + dy
            answer[x][y] = p
            p += 1
    return list(chain(*answer))