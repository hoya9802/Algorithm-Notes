import sys
from collections import deque
input = sys.stdin.readline


n = int(input())
t = list(map(int, input().split()))
data = list(map(int, input().split()))
m = int(input())
c = map(int, input().split())

if sum(t) == n:
    print(*c)
    quit()

tmp = deque([x for x, check in zip(data, t) if check == 0])

for i in c:
    tmp.appendleft(i)

print(' '.join([str(tmp[i]) for i in range(-1,-(m+1),-1)]))