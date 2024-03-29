def solution(s):
    answer = []
    for word in s.split(' '):
        res = ''
        for idx, alp in enumerate(word):
            if idx % 2 == 0:
                res += alp.upper()
            else:
                res += alp.lower()
        answer.append(res)
        
    return ' '.join(answer)