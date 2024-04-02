def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i in range(0,len(score),m):
        if i + m <= len(score):
            answer += score[i+m-1]
            
    answer *= m
    return answer