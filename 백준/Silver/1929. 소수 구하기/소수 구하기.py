import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [False] * (m+1)
lst[1] = True
for i in range(2, int(math.sqrt(m))+1):
    j = 2
    while i * j <= m:
        lst[i*j] = True
        j += 1
for i in range(n,m+1):
    if not lst[i]:
        print(i)