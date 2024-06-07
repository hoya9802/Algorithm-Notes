import sys
input = sys.stdin.readline

n, m = map(int, input().split())
x, y, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
clean = [[0] * m for _ in range(n)]

movement = [(-1,0), (0,1), (1,0), (0,-1)]

def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3
res = 1
clean[x][y] = 1
while 1:
    time = 0
    for _ in range(4):
        turn_left()
        nx = x + movement[d][0]; ny = y + movement[d][1]
        if graph[nx][ny] == 0 and clean[nx][ny] == 0:
            clean[nx][ny] = 1
            res += 1
            x, y = nx, ny
            break
        else:
            time += 1

    if time == 4:
        nx = x - movement[d][0]; ny = y - movement[d][1]
        if graph[nx][ny] == 1:
            break
        else:
            x, y = nx, ny

print(res)