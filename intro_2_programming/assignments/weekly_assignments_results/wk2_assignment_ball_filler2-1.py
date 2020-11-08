import math
#create a ball filler program
def ball_filler():
    #usr input for balls to be made
    ball_requested_by_company = int(input("How many bowling balls will be manufactured:  "))
    #diameter of each ball
    daimeter_of_ball =  float(input("What is the diameter of each ball in inches? "))
    #usr input core volume
    inches_cubed = int(input("What is the core volume in inches cubed:  "))
    #calculate volume, convert diameter to radius subtract core colume
    volume = (((4/3) * math.pi) *((daimeter_of_ball/2)**3)-inches_cubed)
    #calculate filler needed
    filler_needed = ball_requested_by_company * volume
    #print to screen
    print("You will need",filler_needed,"inches cubed of filler")
    
ball_filler()