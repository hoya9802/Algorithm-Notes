from collections import deque

def solution(s):
    stack = deque()
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) == 0 or stack.pop() != '(':
                return False
    if len(stack) != 0:
        return False

    return True