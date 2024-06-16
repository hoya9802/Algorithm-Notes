import heapq

def solution(n, k, enemy):
    q = []
    for i in range(len(enemy)):
        heapq.heappush(q, enemy[i])
        if len(q) > k:
            d = heapq.heappop(q)
            if n >= d:
                n -= d
            else:
                return i
    return len(enemy)