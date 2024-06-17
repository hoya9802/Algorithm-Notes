def compress_words(s, token):
    lst = [s[i:i+token] for i in range(0,len(s),token)]
    check_token = lst[0]
    hist = []
    cnt = 1
    for a, b in zip(lst, lst[1:] + ['']):
        if a == b:
            cnt += 1
        else:
            hist.append([cnt, check_token])
            check_token = b
            cnt = 1
    return sum(len(tk) + (len(str(cnt)) if cnt > 1 else 0) for cnt, tk in hist)

def solution(s):
    return min(compress_words(s, i) for i in list(range(1,(len(s)//2)+1))+[len(s)])