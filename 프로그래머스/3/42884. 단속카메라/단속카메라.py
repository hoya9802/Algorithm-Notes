def solution(routes):
    routes.sort(key=lambda x: x[-1])
    new_camera = routes[0][-1]
    ans = 1
    for i in range(1, len(routes)):
        if new_camera < routes[i][0]:
            new_camera = routes[i][-1]
            ans+=1

    return ans