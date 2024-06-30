import sys
from itertools import permutations as pm
input = sys.stdin.readline

n, m = map(int, input().split())

for i in list(pm(range(1,n+1),m)):
    for j in i:
        print(j, end=" ")
    print()