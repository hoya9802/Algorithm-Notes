import sys
from itertools import combinations as cb
input = sys.stdin.readline

n, m = map(int, input().split())

for i in list(cb(range(1,n+1),m)):
    for j in i:
        print(j, end=" ")
    print()