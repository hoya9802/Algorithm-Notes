import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0
    tmp = [-1*x for x in works]
    heapq.heapify(tmp)
    while n > 0:
        big = -1*(heapq.heappop(tmp))
        n -= 1
        heapq.heappush(tmp, -(big-1))
    
    return sum(x**2 for x in tmp)
    
    
    