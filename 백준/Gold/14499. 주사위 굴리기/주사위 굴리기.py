import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

movement = [(0,0), (0,1), (0,-1), (-1,0), (1,0)]

n1 = n2 = n3 = n4 = n5 = n6 = 0
for cmd in list(map(int, input().split())):
    nx = x + movement[cmd][0]; ny = y + movement[cmd][1]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
    if cmd == 1:
        n1, n3, n4, n6 = n4, n1, n6, n3
    elif cmd == 2:
        n4, n1, n3, n6 = n1, n3, n6, n4
    elif cmd == 3:
        n1, n2, n5, n6 = n5, n1, n6, n2
    else:
        n1, n2, n5, n6 = n2, n6, n1, n5
    if graph[nx][ny] == 0:
        graph[nx][ny] = n6
    else:
        n6 = graph[nx][ny]; graph[nx][ny] = 0
    x, y = nx, ny
    print(n1)