#create a my house program

#import graphics library
from graphics import *



#inlcude 3 rectangles, two lines, one circle , one text label
#draw an outdoor scence




def build_house():
# Create window, concept origin credit
    win = GraphWin("Build a house with sunset as outdoor scene with 5 clicks", 500, 500)
    win.setCoords(0,0,10,10)
    teacher_note = Text(Point(5, 9.6), "My concept is based on Zelle's build a house with 5 clicks")
    teacher_note.setSize(10)
    teacher_note.draw(win)
    


# house frame message
    house_frame_message = Text(Point(5,8.9), "Click one time at the bottom left and once at the\n"
                 " right side mid window to create the house frame.")
    house_frame_message.setSize(10)
    house_frame_message.draw(win)

# endpoints to create house frame
    p1 = win.getMouse()
    p1.draw(win)
    x1 = p1.getX()
    y1 = p1.getY()
    p2 = win.getMouse()
    p2.draw(win)
    x2 = p2.getX()
    y2 = p2.getY()

# Create house frame rectangle with color fill
    house_frame_rect = Rectangle(p1,p2)
    house_frame_rect.setOutline("black")
    house_frame_rect.setFill("green")
    house_frame_rect.draw(win)

# house frame click number(s)
    house_frame_p1 = Text(Point(x1 - 0.2 ,y1 - 0.2), "1")
    house_frame_p1.setSize(10)
    house_frame_p1.setTextColor("red")
    house_frame_p1.draw(win)

    house_frame_p2 = Text(Point(x2 + 0.2 ,y2 + 0.2), "2")
    house_frame_p2.setSize(10)
    house_frame_p2.setTextColor("red")
    house_frame_p2.draw(win)

# to create door frame
    p3 = Point(x1+2, y1)
    p4 = Point(x1+2, y1+(.3*(y2-y1)))
    x4 = p4.getX()
    y4 = p4.getY()
    p5 = Point(x1+(0.2*(x2-x1)), y1+(.3*(y2-y1)))
    x5 = p5.getX()
    y5 = p5.getY()
    p6 = Point(x1+(0.2*(x2-x1)), y1)
    x6 = p6.getX()
    y6 = p6.getY()

# message to click to create door
    create_door_message = Text(Point(5,1.4), "Click once inside house to create the door.")
    create_door_message.setSize(10)
    create_door_message.draw(win)

    win.getMouse()

# Draw the door 
    house_door = Polygon(p3, p4, p5, p6)
    house_door.setOutline("black")
    house_door.setFill("blue")
    house_door.draw(win)

# top center of door
    door_top = Line(Point(x4,y4),Point(x5,y5))
    door_top.draw(win)
    x_mid_coord = x5+x4
    y_mid_coord = y5+y4
    p7 = Circle(Point(x_mid_coord, y_mid_coord), 0.03125)
    p7.setFill("cyan")
    p7.draw(win)

#  create door click number
    create_door_click_number = Text(Point(x_mid_coord,y_mid_coord + 0.2), "3")
    create_door_click_number.setSize(10)
    create_door_click_number.setTextColor("red")
    create_door_click_number.draw(win)

# create window
    create_window_message = Text(Point(5,1.1), "Click once inside the frame to create the window.")
    create_window_message.setSize(10)
    create_window_message.draw(win)

# Create window frame square
    p8 = win.getMouse()
    x8 = p8.getX()
    y8 = p8.getY()
    window_frame = Rectangle(Point(x8,y8),(Point(x8+2*(x5-x4),y8+2*(x5-x4))))
    wc = window_frame.getCenter()
    wc_x = wc.getX()
    wc_y = wc.getY()
    window_frame.setOutline("red")
    window_frame.setFill("black")
    window_frame.draw(win)

# window frame click number
    window_frame_click_number = Text(Point(wc_x,wc_y), "4")
    window_frame_click_number.setSize(10)
    window_frame_click_number.setTextColor("red")
    window_frame_click_number.draw(win)

# click to create roof
    create_roof = Text(Point(5,0.8), "Click once on top of house to create the roof.")
    create_roof.setSize(10)
    create_roof.draw(win)

    win.getMouse()

# Create roof frame
    p9 = Point(x1,y2)
    p10 = Point((x1+x2)/2,y2+0.33*((x2+x1)/2))
    x10 = p10.getX()
    y10 = p10.getY()
    roof_frame = Polygon(p2,p9,p10)
    roof_frame.setOutline("orange")
    roof_frame.setFill("blue")
    roof_frame.draw(win)

#roof frame click number
    roof_frame_click_number = Text(Point(x10,y10 + 0.3), "5")
    roof_frame_click_number.setSize(10)
    roof_frame_click_number.setTextColor("red")
    roof_frame_click_number.draw(win)
    
    #create sunset
    p11 = Point(x1,y2)
    p12 =Point((x1+x2)/3,y2+0.39*((x2+x1)/3))
    x11 = p11.getX()
    y11 = p12.getY()
    sunset_center = Point (x11,y11)
    sunset = Circle(sunset_center,.35)
    sunset.setFill("yellow")
    sunset.setOutline("orange")
    sunset.draw(win)
    
    

# click to quit message
    click_to_quit_message = Text(Point(5,0.5), "Click once to quit.")
    click_to_quit_message.setSize(10)
    click_to_quit_message.draw(win)


# wait for click and then quit
    win.getMouse()
    win.close()

build_house()