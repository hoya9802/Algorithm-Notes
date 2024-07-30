import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
limit = int(input())

res = 0
def binary_search(s,e):
    global res
    if s > e:
        return
    mid = (s + e) // 2
    
    total = 0
    for d in data:
        if d > mid:
            total += mid
        else:
            total += d

    if total > limit:
        binary_search(s, mid-1)
    else:
        if res < mid:
            res = mid
        binary_search(mid+1, e)

binary_search(0,max(data))
print(res)