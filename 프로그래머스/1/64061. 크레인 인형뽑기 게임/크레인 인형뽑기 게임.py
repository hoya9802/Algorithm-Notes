from collections import deque
def solution(board, moves):
    answer = 0
    stack = deque()
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0:
                if len(stack) >= 1 and board[i][move-1] == stack[-1]:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(board[i][move-1])
                board[i][move-1] = 0
                break

    return answer