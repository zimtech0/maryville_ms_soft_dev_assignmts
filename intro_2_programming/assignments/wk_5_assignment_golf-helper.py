# create a new golf club recommendation app

# create function
def golf_helper():
# create intro statement
    print('Welcome to the Golf Club Helper !\n ')
    print("Tell me your situation, and I'll recommend a club. \n")
# create user input: hit the green y or n answer
    max_on_green_distance = 20
    on_green = input("Did you hit the ball onto the green (enter y for yes or n for no)? \n ")
# create user input: how far they are from the hole
    distance_from_hole = int(input("How far is the ball from the hole (please enter a whole number)? "))
    
# create process for club selection
    

    # check to see if ball on green
    if  on_green =='y':
    # check distance and compare against max yards on green    
        if distance_from_hole > max_on_green_distance:
    # Warn user they inputted a yardage error    
           print ('Your distance is beyond the green. Please Re-Evaluate and try again')
    # continue with recommendation       
        else:
            print ('I recommend using your Putter.')
    # ball is not on green        
    if on_green =='n':
    # Warn user they inputted a yardage error
        if distance_from_hole <= max_on_green_distance:
            print('You specified you are not on the green but your yardage suggest you are on the green. Please Re-Evaluate and try again.')
    # Process user information based on correct inputs    
        elif distance_from_hole > 200:
            print ('I recommend using your Driver.')
        elif 140 < distance_from_hole < 200:
            print ('I recommend using your 5 - Iron')
        elif 100 < distance_from_hole < 140:
            print ('I recommend using your 9 - Iron')
        else:
            print ('I recommend using a Pitching wedge.')


# call function
golf_helper()