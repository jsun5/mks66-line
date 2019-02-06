from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

for i in range (200):
    plot(screen,color,i,i)
        
display(screen)
save_extension(screen, 'img.png')
