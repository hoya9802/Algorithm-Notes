import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dp = [[0] * (k+1) for _ in range(n+1)]

l = [(0,0)]
for _ in range(n):
    l.append(tuple(map(int, input().split())))

for i in range(1,n+1):
    weight = l[i][0]; value = l[i][1]
    for j in range(1,k+1):
        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(value + dp[i-1][j-weight], dp[i-1][j])

print(dp[-1][-1])