import sys
input = sys.stdin.readline

s = input().rstrip()
n = int(input())
dp = [[0] * len(s) for _ in range(26)]

check_box = []
res = [0] * n
for c in range(n):
    a, l, r = input().split()
    if a not in check_box:
        check_box.append(a)
        dp[ord(a)-97] = [1 if w == a else 0 for w in s]
        for i in range(1, len(s)):
            dp[ord(a)-97][i] += dp[ord(a)-97][i-1]
        dp[ord(a)-97] += [0]

    res[c] = dp[ord(a)-97][int(r)] - dp[ord(a)-97][int(l)-1]

print(*res, sep='\n')