import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = set(); b = set()
for idx in range(n+m):
    if idx < n:
        a.add(input().rstrip())
    else:
        b.add(input().rstrip())

res = sorted(list(a & b))
print(len(res))
for i in res:
    print(i)