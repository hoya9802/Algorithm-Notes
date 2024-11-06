import sys
n = int(sys.stdin.readline())
dp = [0] * (n+1)
if n ==0:
    print(0)
    exit()

def fibo(x):
    if x in (1,2):
        return 1
    if dp[x] != 0:
        return dp[x]
    dp[x] = fibo(x-1) + fibo(x-2)
    return dp[x]

print(fibo(n))