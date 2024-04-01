def solution(s, skip, index):
    answer = ''
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    for sk in skip:
        alphabets = alphabets.replace(sk,'')

    for w in s:
        answer += alphabets[(alphabets.index(w)+index) % len(alphabets)]
           
    return answer