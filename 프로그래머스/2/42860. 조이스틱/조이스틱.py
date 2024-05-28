def check_vert(x):
    return min((ord('Z')+1) - ord(x), ord(x) - ord('A'))

def solution(name):
    res = 0
    hori_min_move = len(name) - 1
    for idx, val in enumerate(name):
        res += check_vert(val)
        nxt = idx + 1
        while nxt < len(name) and name[nxt] == 'A':
            nxt += 1
        hori_min_move = min(hori_min_move, idx*2 + len(name)-nxt, idx + 2*(len(name)-nxt))
    return res + hori_min_move