def solution(X, Y):
    answer = ''
    for i in range(9,-1,-1):
        if X.count(str(i)) > 0 and Y.count(str(i)) > 0:
            answer += str(i) * min(X.count(str(i)), Y.count(str(i)))

    if answer == '':
        answer = '-1'
    elif answer.count('0') == len(answer):
        answer = str(0)
    return answer