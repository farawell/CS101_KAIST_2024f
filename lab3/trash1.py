################################################
# Author: Yohan Park (farawell777@kaist.ac.kr) #
################################################

from cs1robots import *

def face_back(robot):
    if not robot.front_is_clear():
        robot.turn_left()
        robot.turn_left()
        print(f'{robot} is now facing opposite direction')
        return

def turn_right(robot):
    for _ in range(3):
        robot.turn_left()

def dump_trash(robot):
    while robot.carries_beepers():
        robot.drop_beeper()

def main():
    # Your code must work for all world files below.
    load_world( "worlds/trash1.wld" )
    # load_world( "worlds/trash2.wld" )

    hubo = Robot()
    hubo.set_trace('red')

    while hubo.front_is_clear():
        hubo.move()
        if(hubo.on_beeper()):
            while hubo.on_beeper():
                hubo.pick_beeper()

    face_back(hubo)

    while hubo.front_is_clear():
        hubo.move()
    turn_right(hubo)
    hubo.move()
    dump_trash(hubo)

    face_back(hubo)
    hubo.move()
    hubo.turn_left()    

main()