n = int(input())
for i in range(1, n+1):
    print(' '*(n-i)+'*'*(2*i-1))
x = 1
for i in range(n-1,-1,-1):
    print(' '*(x)+'*'*(2*i-1))
    x += 1