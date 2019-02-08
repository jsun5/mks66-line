from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

#for i in range (200):
 #   plot(screen,color,i,i)

#octant 1
draw_line(20,20,15,80,screen,color)
draw_line(20,20,80,80,screen,color)
draw_line(20,20,85,80,screen,color)
draw_line(20,20,140,80,screen,color)
draw_line(20,20,280,80,screen,color)
draw_line(20,20,280,50,screen,color)
draw_line(20,20,280,25,screen,color)
draw_line(20,20,280,20,screen,color)

#octant 2
draw_line(300,300,400,400,screen,color)
draw_line(300,300,400,500,screen,color)
draw_line(300,300,400,600,screen,color)
draw_line(300,300,300,500,screen,color)
draw_line(300,300,400,310,screen,color)

display(screen)
save_extension(screen, 'img.png')
