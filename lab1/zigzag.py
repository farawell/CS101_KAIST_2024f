################################################
# Author: Yohan Park (farawell777@kaist.ac.kr) #
################################################

from cs1robots import *

def move_nine_block(robot):
    for _ in range(9):
        robot.move()

def turn_right(robot):
    for _ in range(3):
        robot.turn_left()

def main():
    # Create the world and the robot
    create_world()
    hubo = Robot()
    hubo.set_trace('blue') # In blue
    hubo.turn_left()

    for i in range(5):
        move_nine_block(hubo)
        turn_right(hubo)
        hubo.move()
        turn_right(hubo)
        move_nine_block(hubo)

        if i < 4:
            hubo.turn_left()
            hubo.move()
            hubo.turn_left()

main()