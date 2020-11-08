#create a gradient bar program

#import graphics library
from graphics import *


def main():
    win = GraphWin("Gradient Bar", 400, 200)
    bar1_rect = Rectangle(Point(67,0),Point(0,400))
    color_a = color_rgb(0, 0, 0)
    bar1_rect.setFill(color_a)
    bar1_rect.draw(win)
    
    bar2_rect = Rectangle(Point(134,0),Point(67,400))
    color_b = color_rgb(0, int(255/6), 0)
    bar2_rect.setFill(color_b)
    bar2_rect.draw(win)
    
    bar3_rect = Rectangle(Point(201,0),Point(134,400))
    color_c = color_rgb(0, int(255/5), 0)
    bar3_rect.setFill(color_c )
    bar3_rect.draw(win)
    
    bar4_rect = Rectangle(Point(268,0),Point(201,400))
    color_d = color_rgb(0, int(255/4), 0)
    bar4_rect.setFill(color_d)
    bar4_rect.draw(win)
    
    bar5_rect = Rectangle(Point(335,0),Point(268,400))
    color_e = color_rgb(0, int(255/3), 0)
    bar5_rect.setFill(color_e)
    bar5_rect.draw(win)
    
    bar6_rect = Rectangle(Point(400,0),Point(335,400))
    color_f = color_rgb(0, int(255/2), 0)
    bar6_rect.setFill(color_f)
    bar6_rect.draw(win)
        
    win.getMouse()
    win.close()

main()