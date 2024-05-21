def solution(k, ranges):
    ans = []; res = []
    while k != 1:
        res.append(k)
        if k % 2 == 0:
            k //= 2
            continue
        k = k * 3 + 1
    res.append(k)
    
    for i in range(len(res)-1):
        res[i] = min(res[i], res[i+1]) + (abs(res[i+1]-res[i]) / 2)
    res.pop()
    
    for i in ranges:
        a, b = i
        if a > len(res)+b:
            ans.append(-1.0)
            continue
        ans.append(float(sum(res[a:(len(res)+b)])))
    return ans