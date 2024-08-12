import sys
input = sys.stdin.readline

while 1:
    cmd = input().rstrip()
    if cmd == '.':
        break
    
    s_lst = []
    for c in list(cmd):
        if c in ['(', ')', '[', ']']:
            s_lst.append(c)
    
    stack = []
    for s in s_lst:
        if s in ['(', '[']:
            stack.append(s)
        else:
            if not stack:
                print('no')
                break
            else:
                if s == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        print('no')
                        break
                else:
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        print('no')
                        break
    else:
        if stack:
            print('no')
        else:
            print('yes')