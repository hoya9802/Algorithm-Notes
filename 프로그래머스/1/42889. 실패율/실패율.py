def solution(N, stages):
    answer = []
    for n in range(1, N+1):
        n_stage = stages.count(n)
        if len(stages) != 0:
            answer.append(n_stage/len(stages))
        else:
            answer.append(0)
        if n in stages:
            stages = [x for x in stages if x != n]
    indexed_list = [(value, index) for index, value in enumerate(answer)]
    sorted_list = sorted(indexed_list, key=lambda x: (-x[0], x[1]))
    res = [index+1 for value, index in sorted_list]
    
    return res