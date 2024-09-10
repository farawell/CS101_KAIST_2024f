################################################
# Author: Yohan Park (farawell777@kaist.ac.kr) #
################################################

from cs1robots import *

def turn_right(robot):
    for _ in range(3):
        robot.turn_left()

def move_six_blocks(robot):
    for _ in range(6):
        robot.move()

def move_right_and_up(robot):
    robot.move()
    robot.turn_left()
    robot.move()
    turn_right(robot)
    robot.pick_beeper()

def move_left_and_down(robot):
    robot.move()
    robot.turn_left()
    robot.move()
    turn_right(robot)
    robot.pick_beeper()

def collect_two_rows(robot, last):
    for _ in range(5):
        move_right_and_up(robot)
    
    robot.move()
    turn_right(robot)
    robot.move()
    turn_right(robot)
    robot.pick_beeper()

    for _ in range(5):
        move_left_and_down(robot)
    
    if not last:
        robot.turn_left()
        robot.move()
        robot.turn_left()
        robot.move()
        robot.pick_beeper()
    
def main():
    # Create the world and the robot
    load_world('worlds/harvest2.wld')
    hubo = Robot()

    hubo.turn_left()
    move_six_blocks(hubo)
    turn_right(hubo)
    hubo.pick_beeper()

    for i in range(3):
        if i < 2:
            collect_two_rows(hubo, False)
        else:
            collect_two_rows(hubo, True)

main()