import sys
input = sys.stdin.readline

def line_checker(n):
    if n % 2 == 0:
        return True
    return False

n = int(input())


s =  1; l = 1
while n > s:
    l += 1; s += l

checker = line_checker(l)
if checker:
    print(f'{l-(s-n)}/{(s-n)+1}')
else:
    print(f'{(s-n)+1}/{l-(s-n)}')
