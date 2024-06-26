import sys, heapq
input = sys.stdin.readline

n = int(input())
pre_q = []; post_q = []

for i in range(n):
    num = int(input())
    if i % 2 == 0:
        heapq.heappush(pre_q, -num)
    else:
        heapq.heappush(post_q, num)
    if len(pre_q) > 0 and len(post_q) > 0:
        pre_check = -1*pre_q[0]
        post_check = post_q[0]
        if pre_check > post_check:
            heapq.heappush(post_q, -heapq.heappop(pre_q))
            heapq.heappush(pre_q, -heapq.heappop(post_q))
        print(-1*pre_q[0])
    else:
        print(-1*pre_q[0])