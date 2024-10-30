n = int(input()); line = 1

while n > line:
    n -= line
    line += 1

if line % 2 == 0:
    b = n; m = line + 1 - n
elif line % 2 != 0:
    b = line + 1 -n; m = n

print(f'{b}/{m}')