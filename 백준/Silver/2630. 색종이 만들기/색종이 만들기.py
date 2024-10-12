import sys
input = sys.stdin.readline

def distinguish(x,y,l):
    check = arr[x][y]
    halfcut = l // 2
    flag = False
    for i in range(x, x+l):
        for j in range(y, y+l):
            if check != arr[i][j]:
                flag = True
                distinguish(x,y,halfcut)
                distinguish(x+halfcut,y,halfcut)
                distinguish(x, y+halfcut, halfcut)
                distinguish(x+halfcut,y+halfcut,halfcut)
                break
        if flag:
            break
    else:
        colorbox[check] += 1


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
colorbox = [0,0]

distinguish(0,0,n)
print('\n'.join(map(str, colorbox)))