def check_rank(n):
    rank = 6 - n + 1
    if rank == 7:
        rank = 6
    return rank

def solution(lottos, win_nums):
    zero_count = lottos.count(0)
    lottos_set = set(lottos); win_nums_set = set(win_nums)
    l_and_w = (lottos_set & win_nums_set)
    res = [check_rank(len(l_and_w) + zero_count), check_rank(len(l_and_w))]
    
    return res