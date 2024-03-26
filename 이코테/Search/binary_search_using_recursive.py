n, target = map(int, input().split())
array = list(map(int, input().split()))

def binary_search(array, target, start, end):
    if start > end:
        return False
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

result = binary_search(array, target, 0, n-1)
if result == False:
    print('원소가 존재하지 않습니다.')
else:
    print(result + 1) # 인덱스 값이 아닌 몇번째 순서에 위치했는지 알려주기 위해 result + 1를 함

"""
원소가 존재할때:
input:
10 7
1 3 5 7 9 11 13 15 17 19
output:
4

원소가 존재하지 않을때:
input:
10 6 
1 3 5 7 9 11 13 15 17 19 
output:
원소가 존재하지 않습니다.
"""