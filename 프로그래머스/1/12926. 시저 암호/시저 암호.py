# # # A:65 Z:90 | a:97 z:122
# # my solution
def solution(s, n):
    answer = ''
    for i in s:
        if ord(i) == 32:
            answer += i
            continue
        sn = ord(i) + (n%26)
        if 65<=ord(i)<=90 and sn > 90:
            answer += chr(65+(sn-90-1))
            continue
        if 97<=ord(i)<=122 and sn > 122:
            answer += chr(97+(sn-122-1))
            continue
        else:
            answer += chr(sn)
    return answer

# best solution
def solution(s, n):
    s = list(s)
    print(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)