array = [7, 5, 0, 3, 1, 6, 2, 4, 8]

def selection_sort(array, reverse = False): 
    for i in range(len(array)):
        min_index = i
        for j in range(i, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[min_index], array[i] = array[i], array[min_index]
    if reverse == True:
        array.reverse()

# When reverse is True:
selection_sort(array, reverse=True)
print(array)
# When reverse is False
selection_sort(array)
print(array)

"""
output:
[8, 7, 6, 5, 4, 3, 2, 1, 0]
[0, 1, 2, 3, 4, 5, 6, 7, 8]
"""