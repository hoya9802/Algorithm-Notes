def solution(A, B):
    n = len(A)
    A.sort(reverse=True)
    B.sort(reverse=True)
    i, j = 0, 0
    ans = 0
    while i < n and j < n:
        if A[i] < B[j]:
            ans += 1
            j += 1
        i += 1
            
    return ans