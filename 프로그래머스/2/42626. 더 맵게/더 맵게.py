import heapq

def mix_sco(a, b):
    return a + (b * 2)

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while len(scoville) >= 2 and scoville[0] < K:
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        tmp = mix_sco(a, b)
        heapq.heappush(scoville, tmp)
        answer += 1
    if len(scoville) == 1 and scoville[0] < K:
        return -1
    return answer