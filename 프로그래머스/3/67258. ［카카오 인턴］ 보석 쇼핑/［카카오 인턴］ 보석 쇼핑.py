from collections import defaultdict

def solution(gems):
    gem_types = len(set(gems))
    n = len(gems)
    
    answer = [0, n - 1]
    counter = defaultdict(int)
    
    start, end = 0, 0
    counter[gems[0]] = 1
    
    while start < n and end < n:
        if len(counter) == gem_types:

            if (end - start) < (answer[1] - answer[0]):
                answer = [start, end]
            
            counter[gems[start]] -= 1
            if counter[gems[start]] == 0:
                del counter[gems[start]]
            start += 1
        else:
            end += 1
            if end < n:
                counter[gems[end]] += 1
    
    return [answer[0] + 1, answer[1] + 1]
