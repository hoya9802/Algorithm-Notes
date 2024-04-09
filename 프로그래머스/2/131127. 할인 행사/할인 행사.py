from collections import defaultdict

def solution(want, number, discount):
    cnt = 0
    for i in range(0, len(discount)-9):
        want_dict = defaultdict(int, {name:n for name, n in zip(want, number)})
        tmp = discount[i:10+i]
        for n in tmp:
            if n in want_dict.keys():
                want_dict[n] -= 1
        check = True
        for c in want_dict.values():
            if c > 0:
                check = False
                break
        if check:
            cnt += 1
    
    return cnt