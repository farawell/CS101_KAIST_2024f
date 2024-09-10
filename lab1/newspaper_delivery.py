################################################
# Author: Yohan Park (farawell777@kaist.ac.kr) #
################################################

from cs1robots import *

def turn_right(robot):
    for _ in range(3):
        robot.turn_left()

def up_one_step(robot):
    robot.turn_left()
    robot.move()
    turn_right(robot)
    robot.move()
    robot.move()

def down_one_step(robot):
    robot.move()
    robot.move()
    robot.turn_left()
    robot.move()
    turn_right(robot)

def main():
    # Create the world and the robot
    load_world('worlds/newspaper.wld')
    hubo = Robot(beepers=1)
    
    hubo.move()

    for _ in range(4):
        up_one_step(hubo)
    
    hubo.drop_beeper()
    hubo.turn_left()
    hubo.turn_left()

    for _ in range(4):
        down_one_step(hubo)

    hubo.move()

main()