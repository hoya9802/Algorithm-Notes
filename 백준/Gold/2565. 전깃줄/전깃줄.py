import sys
input = sys.stdin.readline

def solution(lst, n):
    dp = [1] * n
    for i in range(len(lst)):
        for j in range(i):
            if lst[i] > lst[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

n = int(input())

lst = []
for _ in range(n):
    a, b = map(int, input().split())
    lst.append((a,b))

lst.sort(key=lambda x: x[0])

bl = []
for a, b in lst:
    bl.append(b)

print(n-solution(bl, n))