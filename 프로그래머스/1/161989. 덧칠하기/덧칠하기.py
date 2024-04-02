def solution(n, m, section):
    answer = 1
    st = section[0]
    for p in section:
        if (st + m - 1) < p:
            st = p
            answer += 1
    
    return answer