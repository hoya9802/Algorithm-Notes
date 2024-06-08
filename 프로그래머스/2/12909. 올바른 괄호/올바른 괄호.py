# solve 13

def solution(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if not stack or stack.pop() != '(':
                return False
    if stack:
        return False
    return True