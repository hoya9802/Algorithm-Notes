import sys
input = sys.stdin.readline

n = int(input())

def drawing_star(n):
    if n == 1:
        return ['*']
    star = drawing_star(n//3)
    L = []
    for s in star:
        L.append(s*3)
    for s in star:
        L.append(s+' '*(n//3)+s)
    for s in star:
        L.append(s*3)
    return L

print('\n'.join(drawing_star(n)))