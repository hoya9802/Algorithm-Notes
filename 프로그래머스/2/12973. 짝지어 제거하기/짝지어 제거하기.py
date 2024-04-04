from collections import deque

def solution(s):
    answer = 0
    stack = deque()
    for i in s:
        if len(stack) >= 1 and stack[-1] == i:
            stack.pop()
            continue
        stack.append(i)
    if len(stack) != 0:
        return 0
    return 1