import sys
input = sys.stdin.readline

n, d = map(int, input().split())

road = [[] for _ in range(d+1)]

for _ in range(n):
    a, b, c = map(int, input().split())
    if a > d or b > d:
        continue
    road[b].append((a,c))

dp = [0] * (d+1)

for i in range(1,d+1):
    dp[i] = dp[i-1] + 1

    if road[i]:
        for s in road[i]:
            dp[i] = min(dp[i], dp[s[0]]+s[1])

print(dp[-1])
