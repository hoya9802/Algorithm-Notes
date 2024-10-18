import sys
from collections import deque

input = sys.stdin.readline


wheel = [deque(map(int, input().strip())) for _ in range(4)]

def rotate_wheels(wheel_num, direction, rotate_list):
    rotate_list[wheel_num] = direction


    if wheel_num > 0 and rotate_list[wheel_num - 1] == 0:
        if wheel[wheel_num][6] != wheel[wheel_num - 1][2]:
            rotate_wheels(wheel_num - 1, -direction, rotate_list)

    if wheel_num < 3 and rotate_list[wheel_num + 1] == 0:
        if wheel[wheel_num][2] != wheel[wheel_num + 1][6]:
            rotate_wheels(wheel_num + 1, -direction, rotate_list)

for _ in range(int(input())):
    t, d = map(int, input().split())
    t -= 1

    rotate_list = [0] * 4

    rotate_wheels(t, d, rotate_list)

    for i in range(4):
        if rotate_list[i] != 0:
            wheel[i].rotate(rotate_list[i])

result = 0
for i in range(4):
    if wheel[i][0] == 1:
        result += 2**i

print(result)