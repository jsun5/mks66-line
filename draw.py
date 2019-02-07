from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    quad = -1
    dy = (y1-y0)
    dx = (x1-x0)
    x = x0
    y = y0
    
    if dy > 0 and dy > 0:
        if dx > dy: quad = 1
        else: quad = 2

            
    if quad is -1:
        pass
    if quad is 1:
        A = dy
        B = -dx
        d = 2A + B
        while x < x1:
            plot(x,y)
            if d>0:
                y++
                d+=2B
            x++
            d+=2A
