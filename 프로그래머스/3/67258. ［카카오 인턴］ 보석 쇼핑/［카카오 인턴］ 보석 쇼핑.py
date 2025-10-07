from collections import defaultdict

def solution(gems):
    n = len(gems)
    gem_type = len(set(gems))
    ans = [0, n]
    start, end = 0, 0
    gem_dict = defaultdict(int)
    gem_dict[gems[end]] += 1
    
    while start < n and end < n:
        if len(gem_dict) == gem_type:
            if (end-start) < (ans[-1]-ans[0]):
                ans = [start, end]
            gem_dict[gems[start]] -= 1
            if gem_dict[gems[start]] <= 0:
                del gem_dict[gems[start]]
            start += 1
        else:
            end += 1
            if end < n:
                gem_dict[gems[end]] += 1
    
    return [ans[0]+1, ans[-1]+1]