array = [7, 5, 0, 3, 1, 6, 2, 4, 8]

def selection_sort(array, reverse=False): # default False
    for i in range(len(array)):
        index = i
        for j in range(i, len(array)):
            if reverse == True:
                if array[index] < array[j]:
                    index = j
            else:
                if array[index] > array[j]:
                    index = j
        array[index], array[i] = array[i], array[index]

selection_sort(array, reverse=True)
print(array)
selection_sort(array)
print(array)

"""
output:
[8, 7, 6, 5, 4, 3, 2, 1, 0]
[0, 1, 2, 3, 4, 5, 6, 7, 8]
"""