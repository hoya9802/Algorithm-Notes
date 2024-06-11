def solution(dirs):
    hist = []
    x, y = 5, 5;
    cmd = ['U', 'D', 'R', 'L']
    movement = [(-1,0), (1,0), (0,1), (0,-1)]
    for d in dirs:
        nx = x + movement[cmd.index(d)][0]; ny = y + movement[cmd.index(d)][1]
        if nx < 0 or nx > 10 or ny < 0 or ny > 10:
            continue
        if [(x,y),(nx,ny)] not in hist and [(nx,ny),(x,y)] not in hist:
            hist.append([(x,y),(nx,ny)])
        x, y = nx, ny
    return len(hist)
        
