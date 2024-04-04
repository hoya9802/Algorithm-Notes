def solution(s):
    num = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for n in num:
        if n in s:
            s = s.replace(n, str(num.index(n)))
    
    return int(s)