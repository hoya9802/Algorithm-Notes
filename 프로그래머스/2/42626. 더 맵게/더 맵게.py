# solve 1

import heapq
def mixed_sco(x, y):
    return x + (y*2)

def solution(scoville, K):
    heapq.heapify(scoville)
    res = 0
    while len(scoville)>=2 and scoville[0] < K:
        res += 1
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, mixed_sco(first, second))
    if scoville[0] < K:
        return -1
    return res