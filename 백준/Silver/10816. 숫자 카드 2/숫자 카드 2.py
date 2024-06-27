import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
arr1 = list(map(int, input().split()))
arr1.sort()
m = int(input())
targets = list(map(int, input().split()))
ac = Counter(arr1)

for t in targets:
    print(ac[t], end=" ")