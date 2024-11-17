from cs1robots import *

USE_SOKOBAN_TILES = False
STAGE = 1  # Stage 1 ~ Stage5

def try_move(hubo):
    ################# COPY & PASTE & MODIFY HERE #################
    def turn_back(robot):
        robot.turn_left()
        robot.turn_left()

    def slide_back(robot):
        turn_back(robot)
        robot.move()
        turn_back(robot)

    def pick_all_beepers(robot):
        while robot.on_beeper():
            robot.pick_beeper()
    
    def drop_all_beepers(robot):
        while robot.carries_beepers():
            robot.drop_beeper()

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

    def count_beeprs_at_front(robot):
        num_beepers = 0
        if robot.front_is_clear():
            robot.move()
            while robot.on_beeper():
                robot.pick_beeper()
                num_beepers += 1
            
            if num_beepers >= 1:
                drop_all_beepers(robot)
            slide_back(robot)

            return num_beepers

    if not hubo.front_is_clear(): return False # Case 1

    # Case 2~6
    if beeper_at_front(hubo):
        beeper_num_at_front = count_beeprs_at_front(hubo)
        if beeper_num_at_front == 1:
            hubo.move()
            if not beeper_at_front(hubo): return True # Case 2
            else: return False # ?
        elif beeper_num_at_front == 2:
            hubo.move()
            if not hubo.front_is_clear(): 
                slide_back(hubo)
                return False # Case 4
            _beepers = count_beeprs_at_front(hubo)
            if _beepers == 0 or _beepers == 1:
                pick_all_beepers(hubo)
                hubo.move()
                drop_all_beepers(hubo)
                slide_back(hubo)
                return True # Case 3
            elif _beepers == 2 or _beepers == 3:
                slide_back(hubo)
                return False # Case 4
            else: return False # More than 3 beepers
        elif beeper_num_at_front == 3:
            hubo.move()
            if not hubo.front_is_clear(): 
                slide_back(hubo)
                return False # Case 6
            _beepers = count_beeprs_at_front(hubo)
            if _beepers == 0 or _beepers == 1:
                hubo.pick_beeper()
                hubo.pick_beeper()
                hubo.move()
                hubo.drop_beeper()
                hubo.drop_beeper()
                slide_back(hubo)
                return True # Case 5
            elif _beepers == 2 or _beepers == 3:
                slide_back(hubo)
                return False # Case 6
            else: return False # More than 3 beepers
        else: return False # More than 3 beepers
    else: 
        hubo.move()
        return True # Case 2
    ##############################################################


def go_north(hubo):
    ##################### COPY & PASTE HERE ######################
    while not hubo.facing_north():
        hubo.turn_left()
    return try_move(hubo)
    ##############################################################
    
    
def go_west(hubo):
    ##################### COPY & PASTE HERE ######################
    while not hubo.facing_north():
        hubo.turn_left()
    hubo.turn_left() # Now hubo faces go_westw
    return try_move(hubo)
    ##############################################################


def go_south(hubo):
    ##################### COPY & PASTE HERE ######################
    while not hubo.facing_north():
        hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()

    return try_move(hubo)
    ##############################################################


def go_east(hubo):
    ##################### COPY & PASTE HERE ######################
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
    hubo = load_world('stage' + str(STAGE) + '.wld', use_tiles_source = USE_SOKOBAN_TILES)
    print("Total movements : ", hubo_actions(hubo))