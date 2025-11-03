import heapq

def solution(jobs):
    start = -1; now = 0
    ans = 0
    count = 0
    n = len(jobs)
    q = []
    while count < n:
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(q, (job[1], job[0]))
        if q:
            cost, time = heapq.heappop(q)
            start = now
            now += cost
            count += 1
            ans += (now - time)
        else:
            now += 1
    
    return ans // n