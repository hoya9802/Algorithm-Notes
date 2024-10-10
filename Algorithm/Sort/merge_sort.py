def merge_sort(arr, s, e):
    if s < e:
        mid = (s+e) // 2
        merge_sort(arr, s, mid)
        merge_sort(arr, mid + 1, e)
        merge(arr, s, mid, e)

def merge(arr, s, mid, e):
    i = s; j = mid + 1
    tmp = []

    while i <= mid and j <= e:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1
    
    while i <= mid:
        tmp.append(arr[i])
        i += 1

    while j <= e:
        tmp.append(arr[j])
        j += 1
    
    i = s; t = 0
    while i <= e:
        arr[i] = tmp[t]
        i += 1; t += 1

lst = list(map(int, input().split()))

merge_sort(lst, 0, len(lst)-1)
print(*lst)

'''
input: [4, 5, 1, 3, 2]
ouput: [1, 2, 3, 4, 5]
'''