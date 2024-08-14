import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)
wl = [0]
for _ in range(n):
    wl.append(int(input()))

for i in range(1,n+1):
    if i == 1:
        dp[i] = wl[i]
    else:
        dp[i] = max(wl[i]+wl[i-1]+dp[i-3], wl[i]+dp[i-2], dp[i-1])
print(dp[-1])