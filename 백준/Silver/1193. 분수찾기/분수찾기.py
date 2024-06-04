import sys
n = int(sys.stdin.readline())
line = 0
end = 0
while n > end:
    line += 1
    end += line
diff = end - n
if line % 2 == 0:
    t = line - diff
    b = diff + 1
else:
    t = diff + 1
    b = line - diff
print(f"{t}/{b}")