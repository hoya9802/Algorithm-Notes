import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]

res = 0
for i in range(len(coin)-1,-1,-1):
    if k // coin[i] != 0:
        res += k // coin[i]
    k %= coin[i]
print(res)