array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def insert_sort(array, reverse=False):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
    if reverse == True:
        array.reverse()

# When reverse is True
insert_sort(array, reverse=True)
print(array)
# When reverse is False
insert_sort(array)
print(array)

"""
output:
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""