import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def merge_sort(lst, s, e):
    if s < e:
        mid = (s+e)//2
        merge_sort(lst, s, mid)
        merge_sort(lst, mid+1, e)
        merge(lst,s,mid,e)

def merge(lst, s, mid, e):
    global ans, cnt
    i = s; j = mid + 1; temp = []
    while i <= mid and j <= e:
        if lst[i] <= lst[j]:
            temp.append(lst[i])
            i += 1
        else:
            temp.append(lst[j])
            j += 1

    while i <= mid:
        temp.append(lst[i])
        i += 1
    while j <= e:
        temp.append(lst[j])
        j += 1

    i = s; t = 0
    while i < j:
        lst[i] = temp[t]
        cnt += 1
        if cnt == k:
            ans = lst[i]
        i += 1; t += 1

n, k = map(int, input().split())
a = list(map(int, input().split()))

cnt = 0; ans = -1
merge_sort(a, 0, n-1)
print(ans)