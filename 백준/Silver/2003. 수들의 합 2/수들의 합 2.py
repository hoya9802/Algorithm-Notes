import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))

end, interval_sum = 0, 0
ans = 0
for start in range(n):
    while end < n and interval_sum < m:
        interval_sum += lst[end]
        end += 1
    if m == interval_sum:
        ans += 1

    interval_sum -= lst[start]
print(ans)