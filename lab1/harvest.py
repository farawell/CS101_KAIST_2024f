################################################
# Author: Yohan Park (farawell777@kaist.ac.kr) #
################################################

from cs1robots import *

def turn_right(robot):
    for _ in range(3):
        robot.turn_left()

def move_five_blocks(robot):
    for _ in range(5):
        robot.move()
        robot.pick_beeper()

def main():
    # Create the world and the robot
    load_world('worlds/harvest1.wld')
    hubo = Robot()
    hubo.move()

    for i in range(3):
        hubo.pick_beeper()
        hubo.turn_left()
        move_five_blocks(hubo)
        turn_right(hubo)
        hubo.move()
        hubo.pick_beeper()
        turn_right(hubo)
        move_five_blocks(hubo)
        if i < 2:
            hubo.turn_left()
            hubo.move()
            hubo.pick_beeper

main()