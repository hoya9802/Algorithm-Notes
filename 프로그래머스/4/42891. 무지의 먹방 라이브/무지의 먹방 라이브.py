import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    q = []
    for name, time in enumerate(food_times):
        heapq.heappush(q,(time, name))
    
    total_times = len(food_times)
    pre_time = 0
    while q:
        t, n = heapq.heappop(q)
        height = t - pre_time
        current_time = height * total_times
        if current_time < k:
            k -= current_time
            pre_time = t
        else:
            heapq.heappush(q, (t, n))
            q.sort(key=lambda x : x[1])
            return q[k%len(q)][1] + 1
        total_times -= 1
    return -1
