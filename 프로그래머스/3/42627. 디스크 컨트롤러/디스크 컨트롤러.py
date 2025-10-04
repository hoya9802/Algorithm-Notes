import heapq

def solution(jobs):
    ans = 0
    curr_time = 0
    start_time = -1
    count = 0
    q = []
    
    while count < len(jobs):
        for j in jobs:
            if start_time < j[0] <= curr_time:
                heapq.heappush(q, (j[-1], j[0]))
                
        if q:
            job = heapq.heappop(q)
            start_time = curr_time
            curr_time += job[0]
            ans += curr_time - job[-1]
            count += 1
        else:
            curr_time += 1
    
    return ans//len(jobs)
        