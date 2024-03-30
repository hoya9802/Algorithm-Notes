def solution(board, h, w):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    answer = 0
    target = board[h][w]
    for i in range(4):
        nx = h + dx[i]; ny = w + dy[i]
        if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
            if board[nx][ny] == board[h][w]:
                answer += 1
    return answer