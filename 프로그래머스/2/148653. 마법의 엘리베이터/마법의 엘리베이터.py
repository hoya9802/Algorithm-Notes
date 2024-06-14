def solution(storey):
    res = 0
    data = list(map(int, str(storey)))
    data.reverse()
    for i in range(len(data)):
        if data[i] > 5:
            res += (10-data[i])
            if i+1<len(data):
                data[i+1] += 1
            else:
                res += 1
        elif data[i] == 5:
            res += 5
            if i+1<len(data) and data[i+1] >= 5:
                data[i+1] += 1
        else:
            res += data[i]
    return res