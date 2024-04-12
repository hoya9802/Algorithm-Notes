def solution(s):
    s = s[2:-2].split('},{')
    s = sorted(s, key=lambda x : len(x))
    stack = []
    
    for i in s:
        tmp = [int(i) for i in i.split(',')]
        for x in tmp:
            if x not in stack:
                stack.append(x)
    
    return stack