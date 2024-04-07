from collections import Counter

def solution(k, tangerine):
    cnt = 0
    tg_dict = Counter(tangerine)
    
    for i in sorted(tg_dict.values(), reverse=True):
        k -= i
        cnt += 1
        if k <= 0:
            break

    return cnt