import sys, math
input = sys.stdin.readline

n, k = map(int, input().split())

res = set()
for i in range(1, int(math.sqrt(n)+1)):
    if n % i == 0:
        res.add(i)
        res.add(n//i)
try:
    print(sorted(res)[k-1])
except IndexError:
    print(0)