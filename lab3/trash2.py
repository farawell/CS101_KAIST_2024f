################################################
# Author: Yohan Park (farawell777@kaist.ac.kr) #
################################################

from cs1robots import *

def turn_right(robot):
    for _ in range(3):
        robot.turn_left()

def is_end(robot):
    if not robot.front_is_clear() and not robot.right_is_clear()\
    or not robot.front_is_clear() and not robot.left_is_clear():
        return True
    
    return False

def move2origin(robot):
    if not robot.facing_north():
        while not robot.facing_north():
            robot.turn_left()
    
    robot.turn_left()
    while robot.front_is_clear():
        robot.move()
    
    robot.turn_left()
    while robot.front_is_clear():
        robot.move()

def move_and_pick(robot):
    robot.move()
    if (robot.on_beeper()):
        while robot.on_beeper():
            robot.pick_beeper()

def main():
    # Your code must work with any of the world files below.
    load_world('worlds/trash3.wld')

    # Robot initialization
    hubo = Robot()
    hubo.set_trace('red')
    touched_wall = 0

    hubo.turn_left()

    while True:
        while hubo.front_is_clear():
            move_and_pick(hubo)
        
        if touched_wall % 2 == 0:
            turn_right(hubo)
            if is_end(hubo): break
            move_and_pick(hubo)
            turn_right(hubo)
        else:
            hubo.turn_left()
            if is_end(hubo): break
            move_and_pick(hubo)
            hubo.turn_left()
        
        touched_wall += 1

    move2origin(hubo)

main()