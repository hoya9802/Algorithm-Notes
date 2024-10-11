import sys
input = sys.stdin.readline

a = []; b= []
a_h, a_w = map(int, input().split())
for _ in range(a_h):
    a.append(list(map(int, input().split())))

b_h, b_w = map(int, input().split())
for _ in range(b_h):
    b.append(list(map(int, input().split())))

res = [[0]*b_w for _ in range(a_h)]
for i in range(a_h):
    for j in range(b_w):
        temp = 0
        for k in range(a_w):
            temp += a[i][k] * b[k][j]
        res[i][j] = temp

print('\n'.join(' '.join(map(str, res[i])) for i in range(a_h)))