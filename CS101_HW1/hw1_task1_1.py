from cs1robots import *  # You must not modify this.


STUDENT_ID_NUMBER = 20190258  # You MUST assign your 8-digit student ID number.


def robot_control(hubo):
    ### START OF CODE SPACE ###

    # helper functions
    def turn_right(robot):
        for _ in range(3): robot.turn_left() 
    
    def go_straigt_n(robot, n):
        for _ in range(n): robot.move()
    
    def drop_beeper_n(robot, n):
        for _ in range(n): robot.drop_beeper()
    
    def command(robot, comm):
        mapping = {'north': 1,
                   'west' : 2,
                   'south': 3,
                   'east' : 4,
                   'jump' : 5
                  }

        drop_beeper_n(robot, mapping[comm])
    
    # main routine
    go_straigt_n(hubo, 5)
    turn_right(hubo)
    command(hubo, 'east')

    go_straigt_n(hubo, 3)
    turn_right(hubo)
    command(hubo, 'south')

    go_straigt_n(hubo, 7)
    hubo.turn_left()
    command(hubo, 'east')

    go_straigt_n(hubo, 4)
    turn_right(hubo)
    command(hubo, 'north')

    go_straigt_n(hubo, 1)

    ### END OF CODE SPACE ###
    pass


# You must not modify this.
def main():
    hubo, start = generate_world_and_robot(STUDENT_ID_NUMBER)
    robot_control(hubo)
    generate_minions(start)


# You must not modify this.
if __name__ == '__main__':
    main()
