import sys
input = sys.stdin.readline

arr = [
    [10],
    [1],
    [2,4,8,6],
    [3,9,7,1],
    [4,6],
    [5],
    [6],
    [7,9,3,1],
    [8,4,2,6],
    [9,1],
]
for _ in range(int(input())):
    a, b = map(int, input().split())
    print(arr[a%10][(b%len(arr[a%10]))-1])
