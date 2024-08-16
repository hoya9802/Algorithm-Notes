import sys
input = sys.stdin.readline

s = input().rstrip()

sl = s.split('-')
res = []

for i in sl:
    tmp = 0
    tl = i.split('+')
    for j in tl:
        tmp += int(j)
    
    if len(res) == 0:
        res.append(tmp)
    else:
        res.append(-tmp)
print(sum(res))