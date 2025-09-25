def kadane(arr):
    n = len(arr)
    dp = [0]
    dp[0] = arr[0]
    ans = arr[0]
    
    for i in range(1, n):
        dp[0] = max(arr[i], dp[0]+arr[i])
        ans = max(ans, dp[0])
    
    return ans

def solution(sequence):
    n = len(sequence)
    arr1 = [sequence[i]*-1 if i%2==0 else sequence[i]*1 for i in range(n)]
    arr2 = [sequence[i]*1 if i%2==0 else sequence[i]*-1 for i in range(n)]
    
    return max(kadane(arr1), kadane(arr2))