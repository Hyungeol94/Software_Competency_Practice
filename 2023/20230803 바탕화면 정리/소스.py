#https://school.programmers.co.kr/learn/courses/30/lessons/161990

def solution(wallpaper):
    lux, luy, rdx, rdy = 0, 0, 0, 0
    for i, row in enumerate(wallpaper):
        if '#' in row:
            lux = i
            break
    for i, col in enumerate(zip(*wallpaper)):
        if '#' in col:
            luy = i
            break
    enumerated_wallpaper = tuple(enumerate(wallpaper))
    for i, row in reversed(enumerated_wallpaper):
        if '#' in row:
            rdx = i
            break
    enumerated_wallpaper = tuple(enumerate(zip(*wallpaper)))
    for i, col in reversed(enumerated_wallpaper):
        if '#' in col:
            rdy = i
            break
    return [lux, luy, rdx+1, rdy+1]
    
        
    