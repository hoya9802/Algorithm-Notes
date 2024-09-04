import sys
input = sys.stdin.readline

for _ in range(int(input())):
    c = int(input())
    res = [0] * 4
    for idx, i in enumerate([25, 10, 5]):
        res[idx] = c // i
        c %= i
    res[-1] = c
    print(*res)