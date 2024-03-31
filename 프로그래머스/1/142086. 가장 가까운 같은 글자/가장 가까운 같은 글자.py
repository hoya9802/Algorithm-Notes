from collections import deque

def solution(s):
    answer = []
    s_dict = {name:0 for name in s}
    stack = []
    for i in range(len(s)):
        if s[i] not in stack:
            s_dict[s[i]] = i
            answer.append(-1)
            stack.append(s[i])
        else:
            answer.append(i-s_dict[s[i]])
            s_dict[s[i]] = i

    return answer