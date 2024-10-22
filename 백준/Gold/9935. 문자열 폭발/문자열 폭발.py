import sys
input = sys.stdin.readline

res = []
s = input().rstrip()
bomb = input().rstrip()
lb = len(bomb)

for i in s:
    res.append(i)
    if ''.join(res[len(res)-lb::]) == bomb:
        for _ in range(lb):
            res.pop()
if res:
    print(*res, sep='')
else:
    print("FRULA")