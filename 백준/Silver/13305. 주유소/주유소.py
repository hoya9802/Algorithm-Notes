import sys
input = sys.stdin.readline

n = int(input())
l = tuple(map(int, input().split()))
c = tuple(map(int, input().split()))

cost = c[0]
dp = [0] * (n)
for i in range(1,n):
    if cost >= c[i-1]:
        cost = c[i-1]
    dp[i] = dp[i-1] + (cost * l[i-1])

print(dp[-1])