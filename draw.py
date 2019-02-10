from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    if(x0>x1):
        draw_line(x1,y1,x0,y0,screen,color)
        pass
    quad = -1
    dy = (y1-y0)
    dx = (x1-x0)
    x = x0
    y = y0
    
    if dy > 0 and dy > 0:
        if dx > dy: quad = 1
        else: quad = 2
    if dy < 0 and dx > 0:
        if dx > abs(dy): quad = 8
        else: quad = 7

    if quad is 1:
        A = dy
        B = -dx
        d = 2*A + B
        while x <= x1:
            plot(screen,color,x,y)
            if d>0:
                y+=1
                d+=2*B
            x+=1
            d+=2*A
    if quad is 2:
        A = dy
        B = -dx
        d = 2*B + A
        while y <= y1:
            plot(screen,color,x,y)
            if d<0:
                x+=1
                d+=2*A
            y+=1
            d+=2*B
    if quad is 8:
        A = dy
        B = -dx
        d = -2*A + B
        while x <= x1:
            plot(screen,color,x,y)
            if d<0:
                y-=1
                d-=2*B
            x+=1
            d+=2*A
    if quad is 7:
        A = dy
        B = -dx
        d = -2*B + A
        while y >= y1:
            plot(screen,color,x,y)
            if d<0:
                x+=1
                d-=2*A
            y-=1
            d+=2*B
    else:
        pass
    #octants 3-6, we can just change x0,x1
    #so call draw_line(x1,y1,x0,y0,screen,color)
