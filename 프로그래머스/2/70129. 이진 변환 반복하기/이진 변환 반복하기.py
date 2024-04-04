from collections import Counter

def solution(s):
    answer = [0,0]
    
    while 1:    
        answer[0] += 1
        if s.count('0') != 0:
            answer[1] += s.count('0')
        s = s.replace('0', '')
        if len(s) == 1:
            return answer
        s = bin(len(s))[2:]
        
    return answer