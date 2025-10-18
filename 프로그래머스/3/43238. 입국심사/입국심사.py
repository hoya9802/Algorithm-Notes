def checker(n, times, time):
    total = 0
    
    for t in times:
        total += (time//t)
        if total >= n:
            return True
    return False

def solution(n, times):
    min_time = min(times) * n
    
    def binary_search(s, e):
        nonlocal min_time
        if s > e:
            return
        mid = (s+e)//2
        
        if checker(n, times, mid):
            min_time = mid
            binary_search(s, mid-1)
        else:
            binary_search(mid+1, e)
    
    binary_search(1, min_time)
    
    return min_time