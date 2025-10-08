def checker(stones, k, people):
    count = 0
    for s in stones:
        if s < people:
            count += 1
            if count == k:
                return False
        else:
            count = 0
    else:
        return True
            
def binary_search(s, e, k, stones):
    global ans
    if e < s:
        return
    mid = (s + e) // 2
    if checker(stones, k, mid):
        if ans < mid:
            ans = mid
        binary_search(mid+1, e, k, stones)
    else:
        binary_search(s, mid-1, k, stones)

ans = 0
        
def solution(stones, k):
    start = 0; end = max(stones)
    
    binary_search(start, end, k, stones)
    
    return ans