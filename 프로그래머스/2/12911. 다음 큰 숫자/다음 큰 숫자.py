def solution(n):
    answer = 0
    i = 1
    while 1:
        temp = bin(n+i)[2:]
        if temp.count('1') == bin(n).count('1'):
            answer = temp
            break
        i += 1
    
    return int(answer,2)