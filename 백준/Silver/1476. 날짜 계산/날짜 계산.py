import sys
input = sys.stdin.readline

e, s, m = map(int, input().split())
year = 1

while 1:
    if (year - e) % 15 + (year - s) % 28 + (year - m) % 19 == 0:
        print(year)
        break
    year += 1
