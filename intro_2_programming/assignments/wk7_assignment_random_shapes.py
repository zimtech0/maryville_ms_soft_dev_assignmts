#txt creation program

import random
print("Enter the drawing file name to create:") #taking input for name for txt file
name = input()
print("Enter the number of shapes to make:") #taking input for no. of lines in txt
lines = int(input())
f= open(name+".txt","w+")
for i in range(lines):
    if random.randrange(0,2) == 0: #if its circle
        x = random.randrange(0,500)
        y = random.randrange(0,500)
        radius = random.randrange(0,min(min(abs(x-500), x), min(abs(y-500), y)))        #Keeping radius in range so that circle doesnt overflow
        r = random.randrange(175,255)
        g = random.randrange(160,255)
        b = random.randrange(192,255)
        f.write("Circle; %d, %d; %d; %d, %d, %d\n" % (x, y, radius, r, g, b)) #writing to file
    else:                           #if its rectangle
        x1 = random.randrange(0,500)
        y1 = random.randrange(0,500)
        x2 = random.randrange(0,500)
        y2 = random.randrange(0,500)
        r = random.randrange(175,255)
        g = random.randrange(160,255)
        b = random.randrange(192,255)
        f.write("Rectangle; %d, %d; %d, %d; %d, %d, %d\n" % (x1, y1, x2, y2, r, g, b)) #writing to file

f.close()#close the file

#shape_painter.py program

import re
from graphics import *
win = GraphWin("My Drawing", 500, 500) #setting drawing window to 500*500px
f= open(name+".txt","r")    #open file in read mode
linebyline = f.readlines() #reading file line by line
for line in linebyline:
    words = re.split("; |, |\n", line)
    if words[0]=="Circle" :
        cir = Circle(Point(int(words[1]), int(words[2])), int(words[3]))
        cir.setFill(color_rgb(int(words[4]), int(words[5]), int(words[6])))
        cir.draw(win)           #drawing circle
    elif words[0]=="Rectangle" :
       rec = Rectangle(Point(int(words[1]), int(words[2])), Point(int(words[3]), int(words[4])))
       rec.setFill(color_rgb(int(words[5]), int(words[6]), int(words[7])))
       rec.draw(win)           #drawing rectangle

win.getMouse()                  #close window on mouse click

win.close()