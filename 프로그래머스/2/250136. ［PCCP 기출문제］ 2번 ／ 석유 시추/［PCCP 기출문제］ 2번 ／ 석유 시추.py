from collections import deque

def solution(land):
    global oils
    visited = [[False] * len(land[0]) for _ in range(len(land))]
    movement = [(-1,0), (0,1), (1,0), (0,-1)]
    oils = {}; now = 1
    def bfs(x, y, now):
        global count
        q = deque(); q.append([x,y])
        count = 1
        visited[x][y] = True
        land[x][y] = now
        while q:
            dx, dy = q.popleft()
            for i in range(4):
                nx = dx + movement[i][0]; ny = dy + movement[i][1]
                if nx < 0 or nx >= len(land) or ny < 0 or ny >= len(land[0]) or visited[nx][ny] == True or land[nx][ny] == 0:
                    continue
                land[nx][ny] = now
                count += 1
                visited[nx][ny] = True
                q.append([nx, ny])
        oils[now] = count
        
    for i in range(len(land[0])):
        for j in range(len(land)):
            if visited[j][i] == False and land[j][i] == 1:
                bfs(j,i,now)
                now += 1
    ans = []
    for i in range(len(land[0])):
        s = set()
        for j in range(len(land)):
            if land[j][i] != 0:
                s.add(land[j][i])
        temp = 0
        for t in s:
            temp += oils[t]
        ans.append(temp)
    return max(ans)