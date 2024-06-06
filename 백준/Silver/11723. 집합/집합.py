import sys

input = sys.stdin.readline
m = int(input())
s = set()

for _ in range(m):
    cmd = list(input().split())
    if len(cmd) == 2:
        num = int(cmd[1])
        if cmd[0] == 'add':
            if num not in s:
                s.add(num)
            else:
                continue
        if cmd[0] == 'remove':
            if num in s:
                s.remove(num)
            else:
                continue
        if cmd[0] == 'check':
            if num in s:
                print(1)
            else:
                print(0)
        if cmd[0] == 'toggle':
            if num in s:
                s.remove(num)
            else:
                s.add(num)
    else:
        if cmd[0] == 'all':
            s = set([x for x in range(1,21)])
        if cmd[0] == 'empty':
            s = set([])
