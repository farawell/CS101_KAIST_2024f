################################################
# Author: Yohan Park (farawell777@kaist.ac.kr) #
# Modiifed from the skeleton code on Alice     #
################################################

from cs1robots import *

# Your code should work with any of the world files below. 

# TIP: Press Ctrl + '/' (or Cmd + '/' if you are using a Mac) 
# to comment out or restore the whole line of the code in the editor.

# load_world('worlds/hurdles1.wld')
# load_world('worlds/hurdles2.wld')
load_world('worlds/hurdles3.wld')

def turn_right(robot):
    for _ in range(3):
        robot.turn_left()

def jump_one_hurdle(robot):
    robot.turn_left()
    robot.move()
    turn_right(robot)
    robot.move()
    turn_right(robot)
    robot.move()
    robot.turn_left()

def main():
    hubo = Robot()
    hubo.set_trace('blue')

    for _ in range(9):
        if hubo.front_is_clear():
            hubo.move()
        else:
            jump_one_hurdle(hubo)

        if hubo.on_beeper():
            break

main()