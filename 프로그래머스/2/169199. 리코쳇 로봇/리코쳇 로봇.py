from collections import deque

def bfs(pos, board, i):
    x, y = pos
    movement = [(-1,0), (0,1), (1,0), (0,-1)]
    while 1:
        x += movement[i][0]; y += movement[i][1]
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] == 'D':
            break
    x -= movement[i][0]; y -= movement[i][1]
    return x, y
        
def solution(board):
    visited = [[-1] * len(board[0]) for _ in range(len(board))]
    start_pos = [0,0]; goal_pos = [0,0]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                start_pos[0] = i; start_pos[1] = j
            if board[i][j] == 'G':
                goal_pos[0] = i; goal_pos[1] = j
    queue = deque([])
    queue.append(start_pos)
    visited[start_pos[0]][start_pos[1]] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = bfs([x,y], board, i)
            if visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append([nx, ny])
    return visited[goal_pos[0]][goal_pos[1]]