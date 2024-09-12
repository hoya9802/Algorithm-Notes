import sys
input = sys.stdin.readline

n = int(input())

dp = [0] + [1] * (n)
for i in range(1, n+1):
    if i in (1,2):  continue
    dp[i] = dp[i-1] + (dp[i-1] - dp[i-2]) + (dp[i-2] - dp[i-3])

print(dp[-1])