import sys
from collections import deque
input = sys.stdin.readline

def rotation(q, p, cnt):
    if cnt > 0:
        q.rotate(-(cnt - 1))
        p.rotate(-(cnt - 1))
    else:
        q.rotate(-cnt)
        p.rotate(-cnt)

n = int(input())
q = deque(range(1, n + 1))
p = deque(map(int, input().split()))

res = []

while q:
    res.append(q.popleft())
    cnt = p.popleft()
    
    if q:
        rotation(q, p, cnt)

print(' '.join(map(str, res)))
