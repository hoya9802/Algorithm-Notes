def solution(n):
    dp = [0] * (n+1)
    dp[2] = 3
    for i in range(3,n+1):
        if i % 2 == 0:
            dp[i] = (dp[i-2] * 3 + sum(x for x in dp[1:i-3] if x > 0) * 2 + 2) % 1000000007
    return dp[n]