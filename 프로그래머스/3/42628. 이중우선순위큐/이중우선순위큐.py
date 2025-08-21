import heapq

def solution(operations):
    queue = []
    for op in operations:
        op = op.split()
        cmd = op[0]; num = int(op[-1])
        
        if cmd == "I":
            heapq.heappush(queue, num)
        else:
            if queue:
                if num < 0:
                    heapq.heappop(queue)
                else:
                    queue.sort()
                    queue.pop()
    if not queue:
        return [0, 0]
    queue.sort()
    return [queue[-1], queue[0]]