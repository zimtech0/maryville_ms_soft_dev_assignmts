# create double side of the river(side 1 and side 2bank of river).

first_bank = {'cannibal': 3, 'missionaries': 3}  #first side
second_bank = {'cannibal': 0, 'missionaries': 0} #second side
boat = {'cannibal': 0, 'missionaries': 0}   


def print_state(river_bank1, river_bank2, river_bank3): # function to print state/steps
   

    msg = """
    Bank 1: {} C, {} M
    Bank 2: {} C, {} M
    Boat  : {} C, {} M
    """

    print(msg.format(river_bank1['cannibal'], river_bank1['missionaries'], river_bank2['cannibal'], river_bank2['missionaries'],
                     river_bank3['cannibal'], river_bank3['missionaries']))


def cross_river(A=first_bank, B=second_bank, boat=boat):
    if all(x == 0 for x in B.values()):  # second_bank is empty
        print_state(A, B, boat)
        A['cannibal'] -= 1  # 1 cannibal leaves first_bank and ...
        boat['cannibal'] += 1  # moving on boat

    A['missionaries'] -= 1  # 1 missionary leaves first_bank and ...
    boat['missionaries'] += 1  # moving on boat
    print_state(A, B, boat)

    if all(x == 0 for x in A.values()):  # first_bank is empty
        boat['cannibal'], boat['missionaries'] = 0, 0  # 1 cannibal and 1 missionary go out of boatat
        B['cannibal'] += 1  # 1 cannibal steps out on second_bank
        B['missionaries'] += 1  # 1 missionary steps out on second_bank
        print_state(A, B, boat)
        return  # final condition is reached

    boat['missionaries'] -= 1  # 1 missionary goes out of boat and 
    B['missionaries'] += 1  #  steps out on second_bank
    print_state(A, B, boat)

    A['cannibal'] -= 1  # 1 cannibal leaves first_bank and ...
    boat['cannibal'] += 1  # moving on boat
    print_state(A, B, boat)

    boat['cannibal'] -= 1  # 1 cannibal goes out of boatat and ...
    B['cannibal'] += 1  # ... steps out on second_bank
    print_state(A, B, boat)

    cross_river(A, B, boat)  

def main(): #main function

    print("C=cannibal,M=Missionary")
    cross_river()
    
if __name__=="__main__":
    main()