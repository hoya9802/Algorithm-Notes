import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
lc = Counter(lst)
m = int(input())
targets = list(map(int, input().split()))
for t in targets:
    if not lc.get(t):
        print(0, end= " ")
    else:
        print(1, end= " ")