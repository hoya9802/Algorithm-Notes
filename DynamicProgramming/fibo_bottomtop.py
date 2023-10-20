# Implement a top-down method using a iteration.

d = [0] * 100
x = 99

d[1], d[2] = 1, 1
for i in range(3, x + 1):
    d[i] = d[i-1] + d[i-2]

print(d[x])

# 218922995834555169026