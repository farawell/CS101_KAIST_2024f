################################################
# Author: Yohan Park (farawell777@kaist.ac.kr) #
################################################

from cs1robots import *

def turn_right(robot):
    for _ in range(3):
        robot.turn_left()

def face_north(robot): 
    while not robot.facing_north():
        robot.turn_left()

def move2origin(robot):
    if not robot.facing_north():
        print("Robot should be facing north")
        return
    
    robot.turn_left()
    while robot.front_is_clear():
        robot.move()
    
    robot.turn_left()
    while robot.front_is_clear():
        robot.move()

def main():
    # create world
    create_world()

    hubo = Robot(orientation='W', avenue=7, street=5)
    hubo.set_trace('red')

    face_north(hubo)
    move2origin(hubo)

main()