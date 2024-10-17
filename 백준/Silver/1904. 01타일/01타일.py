n = int(input())
dp = [0] * (n+1)
for i in range(1,n+1):
    if i == 1:
        dp[i] = 1
        continue
    elif i == 2:
        dp[i] = 2
        continue
    dp[i] = (dp[i-1] + dp[i-2]) % 15746

print(dp[-1])