from collections import deque

def solution(order):
    mainc = [x for x in range(1,len(order)+1)]
    stack = []
    res = 0
    order = deque(order)
    for mc in mainc:
        stack.append(mc)
        while stack and stack[-1] == order[0]:
            stack.pop(); order.popleft()
            res += 1
    return res