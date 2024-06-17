import sys
from collections import deque
input = sys.stdin.readline

N, k = map(int, input().split())
visited = [False] * (100001)
cmd = [-1,1,2]

def bfs(n):
    q = deque([(0, n)])
    visited[n] = True
    while q:
        cnt, n = q.popleft()
        if n == k:
            print(cnt)
            break
        for i in range(3):
            if cmd[i] == -1:
                tn = n - 1
                if tn < 0 or tn > 100000 or visited[tn]:
                    continue
                visited[tn] = True
                q.append((cnt+1, tn))
            elif cmd[i] == 1:
                tn = n + 1
                if tn < 0 or tn > 100000 or visited[tn]:
                    continue
                visited[tn] = True
                q.append((cnt+1, tn))
            elif cmd[i] == 2:
                tn = n * 2
                if tn < 0 or tn > 100000 or visited[tn]:
                    continue
                visited[tn] = True
                q.append((cnt+1, tn))
bfs(N)