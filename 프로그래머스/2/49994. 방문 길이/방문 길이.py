def solution(dirs):
    answer = 0
    x, y = 5,5
    direction = ['U','D','R','L']
    movements = [(-1,0), (1,0), (0,1), (0,-1)]
    direct = []
    for i in dirs:
        nx = x + movements[direction.index(i)][0]
        ny = y + movements[direction.index(i)][1]
        if nx < 0 or ny < 0 or nx > 10 or ny > 10:
            continue
        if [x,y,nx,ny] not in direct and [nx,ny,x,y] not in direct:
            direct.append([x,y,nx,ny])
        x, y = nx, ny
    
    return len(direct)