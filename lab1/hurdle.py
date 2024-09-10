################################################
# Author: Yohan Park (farawell777@kaist.ac.kr) #
################################################

from cs1robots import *

def turn_right(robot):
    for _ in range(3):
        robot.turn_left()

def main():
    # Create the world and the robot
    create_world()
    hubo = Robot()
    hubo.set_trace('blue') # In blue

    for i in range(4):
        hubo.move()
        hubo.turn_left()
        hubo.move()
        turn_right(hubo)
        hubo.move()
        turn_right(hubo)
        hubo.move()
        hubo.turn_left()
    
    hubo.move()
    
main()