import sys
input = sys.stdin.readline

def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n%m)

n = int(input())
lst = [int(input()) for _ in range(n)]

sub_lst = [lst[i]-lst[i-1] for i in range(1, len(lst))]

tmp = sub_lst[0]
for i in sub_lst:
    tmp = gcd(i, tmp)

res = 0
for i in sub_lst:
    d = (i // tmp - 1)
    res += d

print(res)