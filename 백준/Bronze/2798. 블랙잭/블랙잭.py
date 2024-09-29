import sys
from itertools import combinations as cb
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

res = 0
for i in list(cb(arr, 3)):
    tmp = sum(i)
    if tmp <= m and res < tmp:
        res = tmp

print(res)