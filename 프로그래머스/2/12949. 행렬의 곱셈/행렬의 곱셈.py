import numpy as np

def solution(arr1, arr2):
    return np.matmul(arr1,arr2).tolist()

def productMatrix(A, B):
    answer = []

    for i in range(len(A)):
        arr = []
        for j in range(len(B[0])):
            tmp = 0
            for k in range(len(A[0])):
                tmp += A[i][k] * B[k][j]
            arr.append(tmp)
        answer.append(arr)

    return answer