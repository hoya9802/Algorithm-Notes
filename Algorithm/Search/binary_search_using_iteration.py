n, target = map(int, input().split())
array = list(map(int, input().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        if array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False

result = binary_search(array, target, 0, n-1)
if result == False:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)

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