import sys
input = sys.stdin.readline

x, y = map(int, input().split())

wp = (y * 100) // x
target = wp + 1

start = 1; end = x

ans = -1
while start <= end:
    mid = (start + end) // 2
    res = (y+mid)*100 // (x+mid)

    if res >= target:
        ans = mid
        end =mid - 1
    else:
        start = mid + 1

print(ans)