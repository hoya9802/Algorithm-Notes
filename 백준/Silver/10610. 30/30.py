import sys
input = sys.stdin.readline

s = sorted(list(input().rstrip()), reverse=True)

if s[-1] != '0':
    print(-1)
else:
    checker = 0
    for i in s:
        checker += int(i)
    
    if checker % 3 != 0:
        print(-1)
    else:
        print(''.join(s))