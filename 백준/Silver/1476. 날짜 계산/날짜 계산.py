import sys
input = sys.stdin.readline

e, s, m = input().split()
x, y, z = 0, 0, 0
year = 0

while 1:
    x += 1; y += 1; z += 1
    year += 1
    if x > 15:
        x = 1
    if y > 28:
        y = 1
    if z > 19:
        z = 1
    
    if (int(e), int(s), int(m)) == (x, y, z):
        print(year)
        break