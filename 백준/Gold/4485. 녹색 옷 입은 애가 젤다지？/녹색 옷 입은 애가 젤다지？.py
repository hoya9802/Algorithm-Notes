import sys
import heapq
input = sys.stdin.readline
N = int(input())

dx=[-1,0,1,0]
dy=[0,-1,0,1]
cnt = 0

# ✨ 문제 조건대로 진행
while N!=0:
    cnt+=1
    board = [list(map(int,input().split())) for _ in range(N)]
    ch_board = [[-1]*N for _ in range(N)]

    hq = []
    heapq.heappush(hq,(board[0][0],0,0))
    ch_board[0][0] = 0
    
# ✨ dijkstra
    while hq:
        val,x,y = heapq.heappop(hq)
        # ✨ 출력
        if x == N-1 and y == N-1:
            print(f'Problem {cnt}: {val}')
            break
        # ✨ 상하좌우 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx < N and 0<=ny<N and ch_board[nx][ny] == -1:
                ch_board[nx][ny] = 0
                heapq.heappush(hq,(val+board[nx][ny],nx,ny))

    N = int(input())
