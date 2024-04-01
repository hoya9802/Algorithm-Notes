def solution(s, skip, index):
    answer = ''
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    for sk in skip:
        alphabets = alphabets.replace(sk,'')

    for w in s:
        temp = alphabets.index(w) + (index % len(alphabets))
        if temp > len(alphabets)-1:
            temp = temp - len(alphabets)
            answer += alphabets[temp]
            continue
        answer += alphabets[temp]
            
    return answer