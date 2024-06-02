def rotate_90(lst):
    res = [[0] * len(lst[0]) for _ in range(len(lst))]
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            res[i][j] = lst[len(lst)-1-j][i]
    return res
        
def solution(key, lock):
    ex = (2*(len(key)-1))
    for _ in range(4):
        for x in range(len(lock)+ex-len(key)+1):
            for y in range(len(lock)+ex-len(key)+1):
                m = [[0] * (len(lock[0]) + ex) for _ in range(len(lock) + ex)]
                for i in range(len(lock)):
                    for j in range(len(lock[0])):
                        m[i+ex//2][j+ex//2] = lock[i][j]
                for kx in range(len(key)):
                    for ky in range(len(key[0])):
                        m[x+kx][y+ky] += key[kx][ky]
                res = True
                for i in range(len(lock)):
                    for j in range(len(lock[0])):
                        if m[i+ex//2][j+ex//2] != 1:
                            res = False
                if res:
                    return True
        key = rotate_90(key)
    return False