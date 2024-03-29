def solution(t, p):
    l = len(p)
    return len([t[x:x+l] for x in range(len(t))[:(len(t)-l+1)] if t[x:x+l] <= p])