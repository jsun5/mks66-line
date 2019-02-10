from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

#for i in range (200):
 #   plot(screen,color,i,i)

x = 200
for i in range(30):
    draw_line(300,300,x+8*i,400,screen,color)
y = 200
for i in range(30):
    draw_line(300,300,400,y+8*i,screen,color)
x = 200
for i in range(30):
    draw_line(300,300,x+8*i,200,screen,color)
y = 200
for i in range(30):
    draw_line(300,300,200,y+8*i,screen,color)

draw_line(20,20,20,40,screen,color)
draw_line(20,20,40,40,screen,color)
draw_line(20,20,40,20,screen,color)
draw_line(20,20,40,0,screen,color)
draw_line(20,20,20,0,screen,color)
draw_line(20,20,0,0,screen,color)
draw_line(20,20,0,20,screen,color)
draw_line(20,20,0,40,screen,color)

display(screen)
save_extension(screen, 'img.png')
