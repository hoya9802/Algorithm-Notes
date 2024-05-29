# solve 2
def check_win(board, ch):
    for i in range(3):
        if all(x == ch for x in board[i]):
            return True
    for i in range(3):
        if all(ch == board[x][i] for x in range(3)):
            return True
    if all(ch == board[x][x] for x in range(3)):
        return True
    if all(ch == board[2-x][x] for x in range(3)):
        return True
    return False

def solution(board):
    xc = oc = 0
    for i in board:
        xc += i.count('X'); oc += i.count('O')
    if oc < xc or oc > xc + 1:
        return 0
    if (check_win(board,'O') and oc != xc + 1) or (check_win(board, 'X') and oc != xc):
        return 0
    return 1