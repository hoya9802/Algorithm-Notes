import sys
input = sys.stdin.readline

tc = [int(input()) for i in range(int(input()))]
max_val = max(tc)

def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n%m)

dp = [-1] * (max_val + 1)
dp[1] = 3

for i in range(2, max_val+1):
    cnt = 0
    for j in range(1, i):
        if gcd(i,j) == 1:
            cnt += 2
    dp[i] = dp[i-1] + cnt

print('\n'.join(map(str, [dp[i] for i in tc])))