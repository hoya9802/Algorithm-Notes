from collections import defaultdict

def solution(n, lost, reserve):
    res_dict = defaultdict(int,{num:0 for num in range(1, n+1)})
    lost_set = set(lost) - set(reserve)
    res_set = set(reserve) - set(lost)
    answer = n - len(lost_set)
    for i in res_set:
        res_dict[i] += 1

    for i in lost_set:
        if res_dict[i-1] > 0:
            res_dict[i-1] -= 1
            answer += 1
            continue
        if res_dict[i+1] > 0:
            res_dict[i+1] -= 1
            answer += 1

    return answer