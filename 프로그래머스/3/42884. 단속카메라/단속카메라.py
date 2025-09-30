def solution(routes):
    n = len(routes)
    routes.sort(key=lambda x: x[-1])
    point, target = 0, 1
    res = 1
    while point < n and target < n:
        if routes[point][-1] >= routes[target][0]:
            target += 1
            continue
        point = target
        target = point + 1
        res += 1
    
    return res