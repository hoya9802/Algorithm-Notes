import math

def check_div(n):
    ans = []
    end = int(n**(1/2))+1
    for i in range(1,end):
        if n % i == 0:
            ans.append(i); ans.append(n//i)
    ans.sort()
    for i in ans[-1::-1]:
        if i <= n // 2 and i <= 10000000:
            return i
        
def solution(begin, end):
    res = [0] * (end-begin+1)

    for idx, tile in enumerate([x for x in range(begin, end+1)]):
        if tile == 1:
            continue
        temp = check_div(tile)
        res[idx] = temp
    return res