import sys
input = sys.stdin.readline

n = int(input())
arr1 = list(map(int, input().split()))
arr1.sort()
m = int(input())
targets = list(map(int, input().split()))

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end)//2
        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

for t in targets:
    print(binary_search(arr1, t, 0, n-1))
