def solution(n, stations, w):
    result = []; ans = 0
    st = stations[0] - w - 1
    if st > 0:
        result.append(st)

    en = n - (stations[-1] + w)
    if en > 0:
        result.append(en)
        
    if len(stations) > 1:
        for i in range(1,len(stations)):
            md = (stations[i] - w) - (stations[i-1] + w) - 1
            if md > 0:
                result.append(md)

    for i in result:
        tmp = i % (2*w+1)
        if tmp > 0:
            ans += (i//(2*w+1)) + 1
        else:
            ans += (i//(2*w+1))

    return ans