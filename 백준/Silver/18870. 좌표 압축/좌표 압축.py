import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
slst = set(lst)

slst = sorted(slst)

def binary_search(start,end, target):
    while start <= end:
        mid = (start + end) // 2
        if slst[mid] == target:
            return mid
        if slst[mid] > target:
            end = mid-1
        else:
            start = mid+1

for i in lst:
    print(binary_search(0,len(slst)-1, i), end=" ")