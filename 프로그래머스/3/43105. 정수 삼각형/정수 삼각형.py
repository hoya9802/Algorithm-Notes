def solution(triangle):
    max_len = len(triangle[-1])
    dp = [[0] * max_len for _ in range(len(triangle))]
    dp[0][0] = triangle[0][0]
    for i in range(1, len(triangle)):
        for j in range(i+1):
            if j == 0:
                dp[i][j] = triangle[i][j] + dp[i-1][j]
            elif j == max_len-1:
                dp[i][j] = triangle[i][j] + dp[i-1][j-1]
            else:
                dp[i][j] = triangle[i][j] + max(dp[i-1][j], dp[i-1][j-1])
    return max(dp[-1])
            