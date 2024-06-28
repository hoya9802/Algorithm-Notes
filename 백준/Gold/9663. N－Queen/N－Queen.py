import sys
input = sys.stdin.readline

n = int(input())
v1 = [0] * n
v2 = [0] * (2*n)
v3 = [0] * (2*n)

res = 0
def n_queen(i):
    global res
    if i == n:
        res += 1
        return
    for j in range(n):
        if v1[j] == v2[i+j] == v3[i-j] == 0:
            v1[j] = v2[i+j] = v3[i-j] = 1
            n_queen(i+1)
            v1[j] = v2[i+j] = v3[i-j] = 0
n_queen(0)
print(res)