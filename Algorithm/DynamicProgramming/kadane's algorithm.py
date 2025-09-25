"""
Kadane's Algorithm: 연속 부분합의 최댓값을 구하는 알고리즘 (DP)

dp[i] = max(arr[i], dp[i-1] + arr[i])
    - arr[i]            : 현재 원소에서 새로운 부분합을 시작
    - dp[i-1] + arr[i]  : 이전까지의 최대 부분합에 현재 원소를 이어붙임

시간 복잡도: O(n)
공간 복잡도: O(n) (리스트 dp를 사용, 최적화하면 O(1)도 가능)
"""

arr = [10, -1, -3, -2, 1]

def kadane(arr):
    n = len(arr)
    dp = [0] * n    # 공간복잡도 : O(n)
    dp[0] = arr[0]
    ans = arr[0]

    for i in range(1, n):
        dp[i] = max(arr[i], dp[i-1]+arr[i])
        ans = max(dp[i], ans)
    
    print(ans)

kadane(arr)

def kadane_space_optimized(arr):
    dp = [0]        # 공간복잡도 : O(1)
    dp[0] = arr[0]
    ans = arr[0]

    for i in range(1, len(arr)):
        dp[0] = max(arr[i], dp[0]+arr[i])
        ans = max(ans, dp[0])
    
    print(ans)

kadane_space_optimized(arr)