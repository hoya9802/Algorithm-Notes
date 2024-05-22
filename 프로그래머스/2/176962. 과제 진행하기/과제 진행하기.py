def solution(plans):
    lst = []
    for i in plans:
        a, b, c = i
        h,m = map(int, b.split(":"))
        b = h*60+m; c = int(c)
        lst.append([a, b, c])
    lst.sort(key=lambda x: -x[1])

    res = []
    while lst:
        x = lst.pop()
        for idx, val in enumerate(res):
            if val[0] > x[1]:
                res[idx][0] += x[2]
        res.append([x[1]+x[2], x[0]])
    res.sort(key=lambda x: x[0])
    return [x[1] for x in res]