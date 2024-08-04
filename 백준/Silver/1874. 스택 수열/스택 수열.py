import sys
input = sys.stdin.readline

cmd = []; stack = []; check = True
now = 1
for _ in range(int(input())):
    n = int(input())
    while now <= n:
        cmd.append('+')
        stack.append(now)
        now += 1
    if n == stack[-1]:
        cmd.append('-')
        stack.pop()
    else:
        check = False
        break

if check:
    for c in cmd:
        print(c)
else:
    print('NO')