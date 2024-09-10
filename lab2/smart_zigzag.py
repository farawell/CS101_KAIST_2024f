################################################
# Author: Yohan Park (farawell777@kaist.ac.kr) #
# Modiifed from the skeleton code on Alice     #
################################################

from cs1robots import *
import random

# Randomly generated worlds
rows = random.randint(5, 15)
cols = random.randint(5, 15)
if rows == 1:
    cols += 1
create_world(avenues=rows, streets=cols)

def turn_right(robot):
    for _ in range(3):
        robot.turn_left()

def is_end(robot):
    if not robot.front_is_clear() and not robot.right_is_clear()\
    or not robot.front_is_clear() and not robot.left_is_clear():
        return True
    
    return False

def main():
    hubo = Robot()
    hubo.set_trace('blue')

    touched_wall = 0

    hubo.turn_left()

    while True:
        while hubo.front_is_clear():
            hubo.move()
        
        if touched_wall % 2 == 0:
            turn_right(hubo)
            if is_end(hubo): break
            hubo.move()
            turn_right(hubo)
        else:
            hubo.turn_left()
            if is_end(hubo): break
            hubo.move()
            hubo.turn_left()
        
        touched_wall += 1
        
main()