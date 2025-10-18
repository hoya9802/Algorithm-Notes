def kadane(lst):
    dp = [0]
    ans = 0
    for i in range(len(lst)):
        if i == 0:
            dp[0] = lst[0]
        else:
            dp[0] = max(dp[0]+lst[i], lst[i])
        if dp[0] > ans:
            ans = dp[0]
    return ans

def solution(sequence):
    dp1 = [1*sequence[i] if i%2==0 else -1*sequence[i] for i in range(len(sequence))]
    dp2 = [-1*sequence[i] if i%2==0 else 1*sequence[i] for i in range(len(sequence))]
    
    return max(kadane(dp1), kadane(dp2))
    