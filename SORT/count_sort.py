array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

def count_sort(array):
    count = [0] * len(array)
    for i in array:
        count[i] += 1
    
    for i in range(len(count)):
        for j in range(count[i]):
            print(i, end= " ")

count_sort(array)

# 0 0 1 1 2 2 3 4 5 5 6 7 8 9 9