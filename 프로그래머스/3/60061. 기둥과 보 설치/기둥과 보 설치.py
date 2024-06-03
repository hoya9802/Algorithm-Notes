pillar = []; bar = []
def check_pillar(x,y):
    if y == 0 or (y>0 and pillar[x][y-1]):
        return True
    if (x>0 and bar[x-1][y]) or bar[x][y]:
        return True
    return False

def check_bar(x,y,n):
    if (y>0 and pillar[x][y-1]) or (x<n and y >0 and pillar[x+1][y-1]):
        return True
    if 0 < x < n and bar[x-1][y] and bar[x+1][y]:
        return True
    return False

def check_remove(x,y,n):
    for i in range(x-1,x+2):
        for j in range(y,y+2):
            if pillar[i][j] and not check_pillar(i,j):
                return False
            if bar[i][j] and not check_bar(i,j,n):
                return False
    return True

def solution(n, build_frame):
    global pillar, bar
    pillar = [[0] * (n+1) for _ in range(n+1)]
    bar = [[0] * (n+1) for _ in range(n+1)]
    for bf in build_frame:
        x, y, kind, cmd = bf
        if kind == 0:
            if cmd == 1:
                if check_pillar(x,y):
                    pillar[x][y] = 1
            else:
                pillar[x][y] = 0
                if not check_remove(x,y,n):
                    pillar[x][y] = 1

        else:
            if cmd == 1:
                if check_bar(x,y,n):
                    bar[x][y] = 1
            else:
                bar[x][y] = 0
                if not check_remove(x,y,n):
                    bar[x][y] = 1
    res = []
    for i in range(len(pillar)):
        for j in range(len(pillar)):
            if pillar[i][j]:
                res.append([i,j,0])
            if bar[i][j]:
                res.append([i,j,1])

    return sorted(res, key=lambda x: (x[0], x[1], x[2]))