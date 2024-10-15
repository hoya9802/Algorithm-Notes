import sys
input = sys.stdin.readline

n = int(input())
l = tuple(map(int, input().split()))
c = tuple(map(int, input().split()))
dp = [0] * (n)
for i in range(1,n):
    if i == 1:
        dp[i] = l[0] * c[0]
        continue
    dp[i] = min(dp[i-1]+(l[i-1]*c[i-2]), dp[i-1]+(l[i-1]*c[i-1]))

print(dp[-1])