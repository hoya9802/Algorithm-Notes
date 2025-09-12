from collections import defaultdict

def solution(gems):
    gem_type = len(set(gems))
    gems_size = len(gems)
    start, end = 0, 0
    ans = [0, gems_size-1]
    gem_dict = defaultdict(int)
    gem_dict[gems[0]] += 1

    while start < gems_size and end < gems_size:
        if len(gem_dict) == gem_type:
            if (end - start) < (ans[-1] - ans[0]):
                ans = [start, end]
            gem_dict[gems[start]] -= 1
            if gem_dict[gems[start]] == 0:
                del gem_dict[gems[start]]
            start += 1
        else:
            end += 1
            if end < gems_size:
                gem_dict[gems[end]] += 1
    
    return [ans[0]+1, ans[-1]+1]