from collections import deque

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    people = deque(people)
    
    while len(people) != 0:
        if len(people) >= 2 and people[0] + people[-1] > limit:
            people.popleft()
            answer += 1
        elif len(people) >= 2 and people[0] + people[-1] <= limit:
            people.pop()
            people.popleft()
            answer += 1
        elif len(people) == 1:
            answer += 1
            people.pop()

    return answer