def solution(routes):
    routes.sort(key=lambda x: x[-1])
    ans = 0; cur = 0; pointer = 0
    
    while pointer < len(routes):
        if routes[cur][-1] >= routes[pointer][0]:
            pointer += 1
        else:
            cur = pointer
            ans += 1

    return ans+1