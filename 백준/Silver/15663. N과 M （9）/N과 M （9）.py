import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
data = deque(list(map(int, input().split())))

res = set()
def dfs(s):
    if len(s) == m:
        res.add(tuple(s))
        return
    for i in range(len(data)):
        tmp = data.popleft()
        s.append(tmp)
        dfs(s)
        s.pop()
        data.append(tmp)

dfs([])

for i in sorted(res):
    print(' '.join(map(str, i)))