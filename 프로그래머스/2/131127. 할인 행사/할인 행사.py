from collections import Counter

def solution(want, number, discount):
    cnt = 0
    for i in range(0, len(discount)-9):
        want_count = Counter({name:n for name, n in zip(want, number)})
        tmp_count = Counter(discount[i:10+i])
        if want_count == tmp_count:
            cnt += 1
        
    return cnt