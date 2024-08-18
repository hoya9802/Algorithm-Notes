import sys
input = sys.stdin.readline

while 1:
    cmd = input().rstrip().upper()
    if cmd == '#':
        break
    res = 0
    for s in cmd:
        if s in ['A', 'I', 'O', 'U', 'E']:
            res += 1
    print(res)