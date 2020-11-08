#create a color switcher program

#import grahpics lib
from graphics import *
#draw a graphics window
win= GraphWin ('Color Switcher App', 640,320)

#set graphic window background color of choice 
win.setBackground("red")
# waits on mouse click
win.getMouse()
#after mouse click in window background color should change to second color 
win.setBackground("blue")
# of choice and wait for 2nd mouse click
win.getMouse()
# after mouse is clicked in window a final time end program and close window
win.close()