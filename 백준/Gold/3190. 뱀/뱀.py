from collections import deque

def change_dir(cl, op:int):
    movement = [(-1,0), (0,1), (1,0), (0,-1)]
    x, y = cl
    x += movement[op%4][0]; y+= movement[op%4][1]
    return x, y

N = int(input())
K = int(input())
apple_loc = []
for _ in range(K):
    x, y = map(int, input().split())
    apple_loc.append((x-1,y-1))
M = int(input())
move = []
for _ in range(M):
    x, c = input().split()
    move.append((int(x), c))

time = 0; direct = 1; idx = 0
snail = deque([(0,0)])
while 1:
    nx, ny = change_dir(snail[0], direct)
    time += 1
    if nx < 0 or nx >= N or ny < 0 or ny >= N or (nx, ny) in snail:
        break
    snail.appendleft((nx, ny))
    if idx < len(move) and time == move[idx][0]:
        if move[idx][1] == 'L':
            direct -= 1
        else:
            direct += 1
        idx += 1

    if (nx, ny) in apple_loc:
        apple_loc.remove((nx,ny))
        continue
    snail.pop()
print(time)