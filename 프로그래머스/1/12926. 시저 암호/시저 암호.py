# z:122, Z:90 A:65 a:97
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