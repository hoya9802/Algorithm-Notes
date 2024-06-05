import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = list(x for x in range(1, n+1))
res = []
while lst:
    idx = (k-1)%len(lst)
    res.append(lst[idx])
    lst = lst[idx:] + lst[:idx]
    lst.pop(0)

print('<',end="")
for idx, val in enumerate(res):
    if idx == len(res)- 1:
        print(f'{val}>')
        continue
    print(val, end=", ")