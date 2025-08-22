def solution(A, B):
    A.sort()
    B.sort()
    
    result=0; point=0;
    
    for a in A:
        while point < len(A) and B[point] <= a:
            point += 1
        if point < len(A):
            result += 1
            point += 1
        else:
            break
    
    return result