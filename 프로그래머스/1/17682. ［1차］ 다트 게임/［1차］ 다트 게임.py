def solution(dartResult):
    res = []
    score = ['S','D','T']
    temp = ''
    
    for word in dartResult:
        if word.isdigit():
            temp += word
        elif word.isalpha():
            res.append(pow(int(temp), int(score.index(word) + 1)))
            temp = ''
        if word == "*":
            if len(res) > 1:
                res[-2] *= 2
            res[-1] *= 2
        elif word == "#":
            res[-1] *= -1
            
    return sum(res)