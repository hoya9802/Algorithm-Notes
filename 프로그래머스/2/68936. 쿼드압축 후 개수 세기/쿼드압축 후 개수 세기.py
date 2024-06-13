def solution(arr):
    ans = [0,0]
    
    def quad(pos, l):
        x, y = pos
        check = arr[x][y]
        for i in range(l):
            for j in range(l):
                if arr[x+i][y+j] != check:
                    quad([x, y], l//2)
                    quad([x+l//2, y], l//2)
                    quad([x, y+l//2], l//2)
                    quad([x+l//2, y+l//2], l//2)
                    return
        ans[check] += 1
    quad(ans, len(arr))
    
    return ans