import heapq

def solution(jobs):
    start_time = -1
    count = 0
    now = 0
    q = []
    ans = 0
    
    while count < len(jobs):
        for j in jobs:
            if start_time < j[0] <= now:
                heapq.heappush(q, (j[-1], j[0]))
        
        if q:
            job = heapq.heappop(q)
            count += 1
            start_time = now
            now = now + job[0]
            ans += (now - job[-1])
        else:
            now += 1
    
    return ans // len(jobs)