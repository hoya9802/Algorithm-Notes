import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    dp = [[0,0] for _ in range(n+1)]
    for i in range(n+1):
        if i == 0:
            dp[i][0] += 1
        elif i == 1:
            dp[i][1] += 1
        else:
            dp[i][0] = dp[i-1][0] + dp[i-2][0]
            dp[i][1] = dp[i-1][1] + dp[i-2][1]
    print(dp[n][0], dp[n][1])