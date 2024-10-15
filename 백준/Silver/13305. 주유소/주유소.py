import sys
input = sys.stdin.readline

n = int(input())
l = tuple(map(int, input().split()))
c = tuple(map(int, input().split()))
dp = [0] * (n)
for i in range(1,n):
    if i == 1:
        dp[i] = l[0] * c[0]
        continue
    res = int(1e9)
    for j in range(1,i+1):
        temp = l[i-1] * c[j-1]
        if res > temp:
            res = temp
    dp[i] = dp[i-1] + res

print(dp[-1])