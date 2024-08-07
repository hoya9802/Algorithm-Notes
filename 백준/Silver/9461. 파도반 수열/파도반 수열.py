import sys
input = sys.stdin.readline

tl = []
for _ in range(int(input())):
    tl.append(int(input()))

dp = [0] * (max(tl)+1)
for i in range(1, len(dp)):
    if i in [1,2,3]:
        dp[i] = 1
    elif i in [4,5]:
        dp[i] = 2
    else:
        dp[i] = dp[i-5] + dp[i-1]

for i in tl:
    print(dp[i])