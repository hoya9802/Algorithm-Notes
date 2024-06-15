def solution(n, k):
    dp = [1] * (n)
    for i in range(2, n):
        dp[i] = dp[i-1] * i
    temp = [x for x in range(1, n+1)]
    ans = []
    while n > 1:
        ans.append(temp[(k-1)//dp[n-1]])
        temp.remove(temp[(k-1)//dp[n-1]])
        k%=dp[n-1]; n-=1
    ans.append(temp[-1])
    return ans