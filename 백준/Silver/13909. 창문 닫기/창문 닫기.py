import sys
input = sys.stdin.readline

n = int(input())

res = 1
while res**2 <= n:
    res += 1

print(res-1)