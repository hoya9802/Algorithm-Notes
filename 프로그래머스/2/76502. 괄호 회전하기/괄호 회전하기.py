def solution(s):
    cnt = 0
    house = {'(':')', '{':'}', '[':']'}
    
    for _ in range(len(s)):
        stack = []
        for x in s:
            if x in house.keys():
                stack.append(x)
            elif x in house.values():
                if len(stack) == 0:
                    break
                elif house[stack[-1]] == x:
                    stack.pop()
                else:
                    break
        else:
            if len(stack) == 0:
                cnt += 1
                
        s = s[1:] + s[0]
                
    return cnt
