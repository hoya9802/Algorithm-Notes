import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))
lp = len(p)

dp = [0] * (n+lp)

for i in range(len(p), len(dp)):
    tmp=[]

    for j in range(lp):
        if (i-(lp-1)) >= j+1:
            v = dp[i-(j+1)] + p[j]
            tmp.append(v)
    dp[i] = max(tmp)

print(dp[-1])