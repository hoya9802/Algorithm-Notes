import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    lst = list(map(int, input().split())) # lst = [1 1 9 1 1 1]
    q = deque()
    for idx, val in enumerate(lst):     # q = [(1,0), (1,1), (9,2), (1,3), (1,4), (1,5)]
        q.append((val, idx))
    count = 1
    while q:
        if q[0][0] == max(q, key=lambda x: x[0])[0]:
            if q[0][1] == m:
                print(count)
                break
            count += 1
            q.popleft()
        else:
            q.append(q.popleft())