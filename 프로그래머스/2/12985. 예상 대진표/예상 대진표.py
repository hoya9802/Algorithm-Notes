import math

def solution(n,a,b):
    i = 1
    while i <= int(math.log(n,2)):
        if a % 2 != 0:
            a += 1
        if b % 2 != 0:
            b += 1
        if a == b:
            return i
        else:
            a //= 2; b //= 2
        i += 1