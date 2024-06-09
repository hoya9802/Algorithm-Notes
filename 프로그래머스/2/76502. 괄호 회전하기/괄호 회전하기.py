def solution(s):
    res = 0
    s = list(s)
    for _ in range(len(s)):
        s.append(s.pop(0))
        stack = []; flag = True
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            else:
                if not stack:
                    flag = False
                    break
                check = stack[-1]
                if i == ")":
                    if stack.pop() != '(':
                        flag = False
                        break
                if i == "}":
                    if stack.pop() != '{':
                        flag = False
                        break
                if i == ']':
                    if stack.pop() != '[':
                        flag = False
                        break
        if stack:
            flag = False
        if flag == True:
            res += 1
    return res
    
                    