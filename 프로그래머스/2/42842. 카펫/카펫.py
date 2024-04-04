import math

def solution(brown, yellow):
    for i in range(1, int(math.sqrt(yellow))+1):
        if yellow % i == 0:
            if 2*(i+(yellow//i)) == brown-4:
                return [yellow/i+2,i+2]