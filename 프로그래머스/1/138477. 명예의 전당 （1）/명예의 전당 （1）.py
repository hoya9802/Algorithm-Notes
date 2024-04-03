def solution(k, score):
    answer = []
    stack = []
    for i in score:
        stack.append(i)
        stack.sort()
        if len(stack) > k:
            stack = stack[1:]
        answer.append(stack[0])
    return answer