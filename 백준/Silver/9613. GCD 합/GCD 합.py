import sys
from itertools import combinations as cb
input = sys.stdin.readline

def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n%m)

for _ in range(int(input())):
    lst = list(map(int, input().split()))[1:]

    res = 0
    temp = list(cb(lst,2))
    for t in temp:
        tmp = t[0]
        for k in t:
            tmp = gcd(tmp, k)
        res += tmp
    print(res)