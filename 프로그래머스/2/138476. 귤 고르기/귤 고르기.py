from collections import Counter

def solution(k, tangerine):
    lst = list()
    tg_dict = Counter(tangerine)
    tg_val = sorted(tg_dict.values(), reverse = True)
    tg_key = sorted(tg_dict.keys(), reverse = True)
    
    for i in range(len(tg_val)):
        for j in range(tg_val[i]):
            lst.append(tg_key[i])

    return len(set(lst[:k]))