import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * n

data = []
for _ in range(n):
    data.append(int(input()))

for i in range(n):
    if i == 0:
        dp[i] = data[i]
    elif i == 1:
        dp[i] = data[i] + data[i-1]
    else:
        dp[i] = max(dp[i-2]+data[i], data[i] + data[i-1] + dp[i-3])
print(dp[-1])