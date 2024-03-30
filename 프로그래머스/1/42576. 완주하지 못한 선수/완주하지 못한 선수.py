# my solution
def solution(participant, completion):
    ptc = {name:0 for name in participant}
    for i in participant:
        ptc[i] += 1
    for i in completion:
        ptc[i] -= 1
    for i in ptc:
        if ptc[i] != 0:
            return i

import collections
# best solution 1
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

# best solution 2
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer