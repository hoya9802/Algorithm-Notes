# dp solution
import sys
input = sys.stdin.readline

n, d = map(int, input().split())

short = [[] for _ in range(d+1)]

for _ in range(n):
    a, b, c = map(int, input().split())
    if a > d or b > d:
        continue
    short[b].append((a,c))

dp = [0] * (d+1)

for i in range(1, d+1):
    dp[i] = dp[i-1] + 1
    if short[i]:
        for j in short[i]:
            dp[i] = min(dp[i], dp[j[0]] + j[1])

print(dp[-1])
