import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dp = [0] * (k+1)
for _ in range(n):
    weight, value = map(int, input().split())
    for i in range(k, weight-1, -1):
        dp[i] = max(dp[i], dp[i-weight] + value)

print(dp[-1])