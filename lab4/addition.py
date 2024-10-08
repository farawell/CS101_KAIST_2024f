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

def face_opp(robot):
    for _ in range(2):
        robot.turn_left()

def pick_calc_all_beeper(robot):
    beeperNum = 0
    if robot.on_beeper():
        while robot.on_beeper():
            robot.pick_beeper()
            beeperNum += 1
    
    return beeperNum


def move_and_calc(robot):
    beeperNum = 0
    face_north(robot)
    beeperNum += pick_calc_all_beeper(robot)
    robot.move()
    beeperNum += pick_calc_all_beeper(robot)
    face_opp(robot)
    robot.move()
    turn_right(robot)

    return beeperNum

def there_are_beepers(robot):
    turn_right(robot)
    if robot.on_beeper(): res1 = True
    else: res1 = False
    robot.move()
    if robot.on_beeper(): res2 = True
    else: res2 = False

    face_opp(robot)
    robot.move()
    turn_right(robot)

    return res1 or res2

def main():
    # Create the world and the robot
    load_world('worlds/add2.wld')
    hubo = Robot()

    carry = 0

    while hubo.front_is_clear():
        hubo.move()
    face_opp(hubo)

    while True:
        if there_are_beepers(hubo):
            num = move_and_calc(hubo)
            num += carry
            carry = num / 10

            beepers_to_drop = num % 10
            for _ in range(int(beepers_to_drop)):
                hubo.drop_beeper()

            hubo.move()
        else: break

main()