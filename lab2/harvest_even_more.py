################################################
# Author: Yohan Park (farawell777@kaist.ac.kr) #
################################################

from cs1robots import *

def _pick_beeper(robot):
    while robot.on_beeper():
        robot.pick_beeper()

def turn_right(robot):
    for _ in range(3):
        robot.turn_left()

def move_five_blocks_and_up(robot):
    for _ in range(5):
        robot.move()
        _pick_beeper(robot)
    
    turn_right(robot)
    robot.move()
    _pick_beeper(robot)
    turn_right(robot)

def check_wall_and_move(robot):
    while robot.front_is_clear():
        robot.move()
        _pick_beeper(robot)
    
    robot.turn_left()
    robot.move()
    _pick_beeper(robot)
    robot.turn_left()
    
def main():
    # Create the world and the robot
    load_world('worlds/harvest4.wld')
    hubo = Robot()
    hubo.set_trace('blue')

    for i in range(3):
        check_wall_and_move(hubo)

        if i < 2:
            move_five_blocks_and_up(hubo)
        else:
            for _ in range(5):
                hubo.move()
                _pick_beeper(hubo)

main()