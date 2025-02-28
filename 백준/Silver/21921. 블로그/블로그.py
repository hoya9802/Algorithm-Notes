import sys
input = sys.stdin.readline

n, x = map(int, input().split())
arr = [0] * x + list(map(int, input().split()))
dp = [0] * (n+1)
res = -1

for i in range(n):
    dp[i+1] = arr[i+x] + dp[i] - arr[i]
    if dp[i+1] > res:
        res = dp[i+1]

if res == 0:    print('SAD')
else: print(res, sum([1 for x in dp if x == res]), sep='\n')