from cs1robots import *

def go_north(hubo):
    ####################### IMPLEMENT HERE #######################
    while not hubo.facing_north():
        hubo.turn_left()
    if hubo.front_is_clear(): 
        hubo.move()
        return True
    return False 
    ##############################################################
    
    
def go_west(hubo):
    ####################### IMPLEMENT HERE #######################
    while not hubo.facing_north():
        hubo.turn_left()
    hubo.turn_left() # Now hubo faces go_west
    if hubo.front_is_clear():
        hubo.move()
        return True
    return False
    ##############################################################


def go_south(hubo):
    ####################### IMPLEMENT HERE #######################
    while not hubo.facing_north():
        hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()
    if hubo.front_is_clear():
        hubo.move()
        return True
    return False
    ##############################################################


def go_east(hubo):
    ####################### IMPLEMENT HERE #######################
    while not hubo.facing_north():
        hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()
    if hubo.front_is_clear():
        hubo.move()
        return True
    
    return False
    ##############################################################


def hubo_actions(hubo):
    # Repeat this loop,
    # └ Ask user input printing
    #   'Move (w,a,s,d) or exit(x)? '
    #   Perform the correspondent operation for user input,
    #   'w' → Call go_north()
    #   'a' → Call go_west()
    #   's' → Call go_south()
    #   'd' → Call go_east()
    #   'x' → break
    #   Other → Do nothing
    # After the termination of the loop,
    #  return the total count of successful movements
    #  (Total count of go_xx() function returns True)
    ####################### IMPLEMENT HERE #######################
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
    load_world('map.wld')
    hubo = Robot()
    print("Total movements : ", hubo_actions(hubo))
