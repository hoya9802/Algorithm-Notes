# solve 12

def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) == 0 or stack.pop() != '(':
                return False
    if stack:
        return False
    return True