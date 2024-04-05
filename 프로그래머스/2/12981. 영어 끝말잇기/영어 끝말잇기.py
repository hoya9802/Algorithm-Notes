def solution(n, words):
    temp = 0
    for i in range(1,len(words)):
        if words[i-1][-1] != words[i][0] or words[i] in words[0:i]:
            temp = i
            break
    if temp == 0:
        return [0,0]
    else:
        return [(temp%n)+1, (temp//n)+1]