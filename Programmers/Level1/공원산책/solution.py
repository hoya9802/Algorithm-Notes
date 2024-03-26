# my solution
def solution(park, routes):
    op = ['N', 'S', 'W', 'E']
    move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    x, y = 0, 0
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S":
                x, y = i, j

    for route in routes:
        o, d = route.split()
        dx, dy = (move[op.index(o)])

        xx, yy = x, y
        pos_move = True
        for _ in range(int(d)):
            nx = xx + dx; ny = yy + dy
            if 0 <= nx <= len(park)-1 and 0 <= ny <= len(park[0]) -1 and park[nx][ny] != 'X':
                pos_move = True
                xx, yy = nx, ny
            else:
                pos_move = False
                break
        if pos_move:
            x, y = nx, ny

    answer = [x, y]
    return answer