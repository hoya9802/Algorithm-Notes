# This algorithm can remove all specific elements.
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
remove_set = [5, 6]

def remove_all(array, remove_set):
    result = [x for x in array if x not in remove_set]
    return result

b = remove_all(a, remove_set)
print(b)