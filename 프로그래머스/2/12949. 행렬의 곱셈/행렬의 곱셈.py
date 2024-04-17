# solve 1

import numpy as np

# def solution(arr1, arr2):
#     res = np.matmul(arr1, arr2).tolist()
#     return res

def solution(arr1, arr2):
    res = [[0]*len(arr2[0]) for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            tmp = 0
            for k in range(len(arr1[0])):
                tmp += arr1[i][k] * arr2[k][j]
            res[i][j] = tmp
    print(res)
    return res