import sys
input = sys.stdin.readline

arr = []
for _ in range(int(input())):
    s = input().rsplit('.')[-1]
    arr.append(s[:-1])

arr.sort()
checker = arr[0]; cnt = 0
for i in arr:
    if checker == i:
        cnt += 1
    else:
        print(checker, cnt)
        checker = i
        cnt = 1
print(checker, cnt)