res = tuple(map(int, input().split()))
print(min((abs(res[0]-0)), abs(res[1]-0), abs(res[2]-res[0]), abs(res[3]-res[1])))