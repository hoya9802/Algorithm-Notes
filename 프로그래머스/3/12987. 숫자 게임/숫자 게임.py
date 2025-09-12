def solution(A, B):
    n = len(A)
    A.sort(reverse=True)
    B.sort(reverse=True)
    ans = 0
    i, j = 0, 0
    while i < n and j < n:
        if A[i] < B[j]:
            ans += 1
            i += 1; j += 1
        else:
            i += 1
    return ans