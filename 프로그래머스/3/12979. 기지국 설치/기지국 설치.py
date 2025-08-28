def solution(n, stations, w):
    idx = 0; loc = 1; ans = 0
    
    while loc <= n:
        if (idx < len(stations)) and (loc >= stations[idx]-w):
            loc = stations[idx]+w+1
            idx += 1
        else:
            loc += 2*w+1
            ans += 1
    
    return ans