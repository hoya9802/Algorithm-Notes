from collections import defaultdict

def solution(name, yearning, photo):
    answer = []
    ny = defaultdict(int, {n:y for n, y in zip(name, yearning)})
    for p in photo:
        temp = 0
        for n in p:
            temp += ny[n]
        answer.append(temp)
    return answer