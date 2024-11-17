from cs1robots import *

def try_move(hubo):
    ####################### IMPLEMENT HERE #######################
    def turn_back(robot):
        robot.turn_left()
        robot.turn_left()

    def slide_back(robot):
        turn_back(robot)
        robot.move()
        turn_back(robot)

    def beeper_at_front(robot):
        if robot.front_is_clear():
            robot.move()
            if robot.on_beeper():
                slide_back(robot)
                return True
            else:
                slide_back(robot)
                return False
        else: return False

    def pick_all_beepers(robot):
        while robot.on_beeper():
            robot.pick_beeper()
    
    def drop_all_beepers(robot):
        while robot.carries_beepers():
            robot.drop_beeper()

    # One of case 3, 4, 5
    if beeper_at_front(hubo):
        hubo.move()
        if beeper_at_front(hubo):
            slide_back(hubo)
            return False # Case 4

        if not beeper_at_front(hubo) and hubo.front_is_clear():
            pick_all_beepers(hubo)
            hubo.move()
            drop_all_beepers(hubo)
            slide_back(hubo)
            return True # Case 3
        
        else: 
            slide_back(hubo)
            return False # Case 5


    elif hubo.front_is_clear():
        hubo.move()
        return True # Case 2
            
    else: return False # Case 1
    ##############################################################


def go_north(hubo):
    ################# COPY & PASTE & MODIFY HERE #################
    while not hubo.facing_north():
        hubo.turn_left()
    return try_move(hubo)
    ##############################################################
    
    
def go_west(hubo):
    ################# COPY & PASTE & MODIFY HERE #################
    while not hubo.facing_north():
        hubo.turn_left()
    hubo.turn_left() # Now hubo faces go_west

    return try_move(hubo)
    ##############################################################


def go_south(hubo):
    ################# COPY & PASTE & MODIFY HERE #################
    while not hubo.facing_north():
        hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()

    return try_move(hubo)
    ##############################################################


def go_east(hubo):
    ################# COPY & PASTE & MODIFY HERE #################
    while not hubo.facing_north():
        hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()

    return try_move(hubo)
    ##############################################################


def hubo_actions(hubo):
    ##################### COPY & PASTE HERE ######################
    count = 0
    while True:
        dir = input('Move (w,a,s,d) or exit(x)? ')
        if dir == 'x': break
        elif dir == 'w' and go_north(hubo): count += 1
        elif dir == 'a' and go_west(hubo): count += 1
        elif dir == 's' and go_south(hubo): count += 1
        elif dir == 'd' and go_east(hubo): count += 1
        else: pass
    
    return count
    ##############################################################


if __name__ == "__main__":
    load_world('rain2.wld')
    hubo = Robot()
    print("Total movements : ", hubo_actions(hubo))

