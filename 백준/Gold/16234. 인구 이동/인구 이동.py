import sys, math
from collections import deque
input = sys.stdin.readline

n, l, r = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
movement = [(-1,0), (0,1), (1,0), (0,-1)]

def open_gate(x,y, cl, graph_class):
    stack = deque([(x,y)])
    graph_class[x][y] = cl
    while stack:
        x, y = stack.popleft()
        for i in range(4):
            nx = x + movement[i][0]; ny = y + movement[i][1]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            check = abs(graph[x][y] - graph[nx][ny])
            if check < l or check > r or graph_class[nx][ny] != 0:
                continue
            graph_class[nx][ny] = cl
            stack.append((nx,ny))

cnt = 0
while 1:
    cl = 1
    graph_class = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph_class[i][j] == 0:
                open_gate(i,j, cl, graph_class)
                cl+=1
    max_val = max((map(max, graph_class)))
    temp = [[] for _ in range(max_val+1)]
    for i in range(n):
        for j in range(n):
            temp[graph_class[i][j]].append(graph[i][j])
    temp1 = [0] * (max_val + 1)
    for i in range(1,len(temp)):
        temp1[i] = math.floor(sum(temp[i]) / len(temp[i]))
    for i in range(n):
        for j in range(n):
            graph[i][j] = temp1[graph_class[i][j]]
    if max_val == n**2:
        break
    cnt += 1
print(cnt)