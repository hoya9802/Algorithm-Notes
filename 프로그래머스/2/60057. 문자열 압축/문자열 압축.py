def solution(s):
    ans = len(s)
    
    for i in range(1, len(s)//2+1):
        compress = ''
        check = s[0:i]
        cnt = 1
        for j in range(i,len(s),i):
            if check == s[j:j+i]:
                cnt += 1
            else:
                compress += str(cnt) + check if cnt >= 2 else check
                check = s[j:j+i]
                cnt = 1
        compress += str(cnt) + check if cnt >= 2 else check
        ans = min(ans, len(compress))
    return ans