def solution(elements):
    answer = set()
    
    for i in range(len(elements)):
        tmp = elements[i]
        answer.add(tmp)
        for j in range(i+1, i+len(elements)):
            tmp += elements[j%len(elements)]
            answer.add(tmp)
    
    return len(answer)