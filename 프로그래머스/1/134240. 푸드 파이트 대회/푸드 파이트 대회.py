def solution(food):
    answer = ''
    for i in range(1,len(food)):
        answer += str(i)*(food[i]//2)
    return ''.join(list(answer) + ['0'] + list(sorted(answer, reverse=True)))