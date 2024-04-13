from collections import deque

def solution(priorities, location):
    data = deque([(priorities[i],False) if i != location else (priorities[i], True) for i in range(len(priorities))])
    max_val, cnt = 0, 0
    while data:
        max_val = max(data)[0]
        tmp = data.popleft()
        if tmp[0] < max_val:
            data.append(tmp)
            continue
        else:
            cnt += 1
            if tmp[1] == True:
                return cnt