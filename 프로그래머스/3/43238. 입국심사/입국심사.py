def checker(time, n, times):
    tmp = 0
    for t in times:
        tmp += time//t
        if tmp >= n:
            return True
    return False

def solution(n, times):
    ans = min(times) * n
    
    def binary_search(s, e):
        if s > e:
            return
        nonlocal ans
        mid = (s+e)//2
        if checker(mid, n, times):
            ans = mid
            binary_search(s, mid-1)
        else:
            binary_search(mid+1, e)
    
    binary_search(0, ans)
    
    return ans