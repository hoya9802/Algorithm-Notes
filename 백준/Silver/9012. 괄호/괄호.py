import sys
input = sys.stdin.readline

def check(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if not stack or stack.pop() != '(':
                return False
    if stack:
        return False
    return True

for _ in range(int(input())):
    if check(input().rstrip()):
        print('YES')
    else:
        print('NO')