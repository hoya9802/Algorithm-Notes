def solution(n, times):
    res = min(times) * n
    
    def binary_search(s, e):
        nonlocal res
        if s > e:
            return
        mid = (s+e)//2
        p=0
        for t in times:
            p += mid // t
            
        if p < n:
            binary_search(mid+1, e)
        else:
            if res > mid:
                res = mid
            binary_search(s, mid-1)
    
    binary_search(0, res)
    
    return res