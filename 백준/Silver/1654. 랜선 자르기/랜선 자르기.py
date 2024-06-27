import sys
input = sys.stdin.readline

k, m = map(int, input().split())
lst = []
for _ in range(k):
    lst.append(int(input()))

temp = []
def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2; cnt = 0
        for i in arr:
            cnt += i // mid
        if cnt >= target:
            temp.append(mid)
            start = mid+1
        else:
            end = mid-1
    return max(temp)

print(binary_search(lst, m, 1, max(lst)))