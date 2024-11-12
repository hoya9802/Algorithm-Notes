import sys

arr = sys.stdin.readline().rstrip()
res, temp = [], []
flag = False

for s in arr:
    if s == '<':
        if temp:
            res.append(''.join(temp[::-1]))
            temp.clear()
        flag = True
        temp.append(s)
    elif s == '>':
        flag = False
        temp.append(s)
        res.append(''.join(temp))
        temp.clear()
    elif s == ' ' and not flag:
        res.append(''.join(temp[::-1]) + ' ')
        temp.clear()
    else:
        temp.append(s)

if temp:
    res.append(''.join(temp[::-1]))

print(''.join(res))