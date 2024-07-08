import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

dp = [0] * n
dp[0] = 1
for i in range(1,n):
    max_val = 0
    for j in range(i-1,-1,-1):
        if lst[i] > lst[j]:
            if max_val < dp[j]:
                max_val = dp[j]
    dp[i] = max_val + 1
print(max(dp))