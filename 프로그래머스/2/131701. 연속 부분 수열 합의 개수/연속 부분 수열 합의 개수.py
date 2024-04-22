# solve 2

def solution(elements):
    answer = set()
    for i in range(len(elements)):
        temp = elements[i]
        answer.add(temp)
        for j in range(1+i, len(elements)+i):
            temp += elements[j%len(elements)]
            answer.add(temp)
    return len(answer)