import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())), reverse=True)
    b = sorted(list(map(int, input().split())), reverse=True)
    ap, bp, cnt = 0, 0, 0

    while ap < len(a) and bp < len(b):
        if a[ap] > b[bp]:
            cnt += len(b) - bp
            ap += 1
        else:
            bp += 1

    print(cnt)
