import sys
arr = [i for i in sys.stdin.readline().rstrip()]

res = []
temp = []; flag = False
for s in arr:
    if s == '<':
        flag = True
        temp.reverse()
        res.append(''.join(temp))
        temp = []
        temp.append(s)
        continue
    if s == ' ':
        if not flag:
            temp.reverse()
            res.append(''.join(temp)+' ')
            temp = []
            continue
    if s == '>':
        temp.append(s)
        res.append(''.join(temp))
        temp = []
        flag = False
        continue
    temp.append(s)

if temp:
    temp.reverse()
    res.append(''.join(temp))
print(''.join(res))