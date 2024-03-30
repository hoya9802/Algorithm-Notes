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
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]