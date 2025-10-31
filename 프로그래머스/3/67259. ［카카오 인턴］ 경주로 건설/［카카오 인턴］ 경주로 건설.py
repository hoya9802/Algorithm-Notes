from collections import deque

def solution(board):
    n = len(board)
    INF = int(1e9)
    movement = [(0,-1), (1,0), (0,1), (-1,0)]
    
    visited = [[[INF]*4 for _ in range(n)] for _ in range(n)]
    q = deque([])
    
    for d in range(4):
        visited[0][0][d] = 0
        q.append((0, 0, d, 0))

    res = INF
    while q:
        x, y, d, cost = q.popleft()
        
        if (x, y) == (n-1, n-1):
            res = min(res, cost)
            continue
        
        for nd, (mx, my) in enumerate(movement):
            nx, ny = x + mx, y + my
            if 0 <= nx < n and 0 <= ny < n and not board[nx][ny]:
                new_cost = cost + (100 if d == nd else 600)
                
                if visited[nx][ny][nd] > new_cost:
                    visited[nx][ny][nd] = new_cost
                    q.append((nx, ny, nd, new_cost))

    return res
