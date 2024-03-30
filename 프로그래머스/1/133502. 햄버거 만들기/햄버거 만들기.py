def solution(ingredient):
    answer = 0
    res = []
    for i in ingredient:
        res.append(i)
        if res[-4:] == [1,2,3,1]:
            del res[-4:]
            answer += 1
    
    return answer