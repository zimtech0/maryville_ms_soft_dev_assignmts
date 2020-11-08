
from graphics import *

win = g.GraphWin("Happy Face", 200,200)
leftPupil = g.Point(50,75)
leftPupil.draw(win)

rightPupil = g.Point(150,75)
rightPupil.draw(win)

leftEye = g.Circle(leftPupil,20)
leftEye.draw(win)

rightEye = g.Circle(rightPupil,20)
rightEye.draw(win)

leftPupil = g.Point(50,75)
leftPupil.setFill("red")
leftPupil.draw(win)

rightPupil = g.Point(150, 75)
rightPupil.draw(win)

