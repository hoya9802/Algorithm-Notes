import sys
input = sys.stdin.readline

n, c = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()

start = 1
end = arr[-1] - arr[0]
res = 0

while start <= end:
    mid = (start + end) // 2
    current_pos = arr[0]
    cnt = 1
    for i in range(1, n):
        if arr[i] >= current_pos + mid:
            current_pos = arr[i]
            cnt += 1
    if cnt >= c:
        start = mid + 1
        res = mid
    else:
        end = mid - 1

print(res)