import sys
input = sys.stdin.readline

n = int(input())
lst = sorted(list(map(int, input().split())))
x = int(input())
s, e, res = 0, n-1, 0

while s != e:
    tmp = lst[s] + lst[e]
    if tmp == x:
        res += 1
        s += 1
    elif tmp > x:
        e -= 1
    else:
        s += 1

print(res)