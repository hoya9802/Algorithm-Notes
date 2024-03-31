def solution(s):
    answer = 0
    cnt_1, cnt_2 = 0, 0
    for word in s:
        if cnt_1 == cnt_2:
            answer += 1
            k = word
        if k == word:
            cnt_1 += 1
        else:
            cnt_2 += 1
        
    return answer