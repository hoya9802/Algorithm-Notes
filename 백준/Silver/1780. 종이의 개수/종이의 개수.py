import sys
input = sys.stdin.readline

def CountPaper(x, y, l):
    check = arr[x][y]
    thirdcut = l//3; flag = False
    for i in range(x, x+l):
        for j in range(y, y+l):
            if check != arr[i][j]:
                flag = True
                CountPaper(x,y,thirdcut);               CountPaper(x+thirdcut,y,thirdcut);              CountPaper(x+(2*thirdcut),y,thirdcut)
                CountPaper(x,y+thirdcut,thirdcut);      CountPaper(x+thirdcut,y+thirdcut,thirdcut);     CountPaper(x+thirdcut,y+(2*thirdcut),thirdcut)
                CountPaper(x,y+(2*thirdcut),thirdcut);  CountPaper(x+(2*thirdcut),y+thirdcut,thirdcut); CountPaper(x+(2*thirdcut),y+(2*thirdcut),thirdcut)
                break
        if flag:
            break
    else:
        res[check] += 1

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

res = [0,0,0]
CountPaper(0,0,n)
print(res[-1],res[0],res[1],sep='\n')