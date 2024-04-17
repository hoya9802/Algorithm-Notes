def solution(elements):
    answer = set()
    for i in range(len(elements)):
        temp = elements[i]
        answer.add(temp)
        for j in range(i+1,len(elements)+i):
            temp = temp + elements[j%len(elements)]
            answer.add(temp)
    
    return len(answer)