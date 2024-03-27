# my solution
def solution(wallpaper):
    lux = int(1e9); luy = int(1e9); rdx = 0; rdy = 0
    for i, x in enumerate(wallpaper):
        if '#' in [x for x in wallpaper[i]]:
            lux = min(lux, i); rdx = max(rdx, i) + 1
            
    for i in range(len(wallpaper[0])):
        if '#' in [x[i] for x in wallpaper]:
            luy = min(luy, i); rdy = max(rdy, i)+1
        
    answer = [lux, luy, rdx, rdy]
    return answer