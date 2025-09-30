def solution(A, B):
    l = len(A)
    A.sort(reverse=True)
    B.sort(reverse=True)
    res = 0
    p1, p2 = 0, 0
    while p1 < l and p2 < l:
        if A[p1] < B[p2]:
            p1 += 1; p2 += 1
            res += 1
        else:
            p1 += 1
    return res