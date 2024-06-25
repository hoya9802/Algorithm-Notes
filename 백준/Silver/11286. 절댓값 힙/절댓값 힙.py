import sys, heapq
input = sys.stdin.readline

q = []
for _ in range(int(input())):
    cmd = int(input())
    if cmd == 0:
        if not q:
            print(0)
        else:
            tmp = heapq.heappop(q)
            print(tmp[1])
    else:
        heapq.heappush(q, (abs(cmd), cmd))