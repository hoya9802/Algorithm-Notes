import sys
input = sys.stdin.readline

length = sorted(map(int, input().split()))

if length[-1] >= sum(length[:2]):
    length[-1] -= length[-1] - sum(length[:2]) + 1
    print(sum(length))
else:
    print(sum(length))