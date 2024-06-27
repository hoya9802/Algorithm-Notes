import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))

temp = []
def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for i in arr:
            if i > mid:
                total += (i-mid)
        if total < target:
            end = mid-1
        if total >= target:
            temp.append(mid)
            start = mid+1
    print(temp[-1])
binary_search(lst, m, 0, max(lst))