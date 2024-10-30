import sys
from collections import deque
input = sys.stdin.readline

d = deque([])
for _ in range(int(input())):
    cmd = input().split()

    if len(cmd) > 1:
        if cmd[0] == '1': d.appendleft(cmd[-1])
        elif cmd[0] == '2': d.append(cmd[-1])

    if cmd[0] == '3': print(d.popleft() if d else -1)
    if cmd[0] == '4': print(d.pop() if d else -1)
    if cmd[0] == '5': print(len(d))
    if cmd[0] == '6': print(1 if not d else 0)
    if cmd[0] == '7': print(d[0] if d else -1)
    if cmd[0] == '8': print(d[-1] if d else -1)