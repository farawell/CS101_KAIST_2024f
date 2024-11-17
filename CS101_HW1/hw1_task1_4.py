from cs1robots import *  # You must not modify this.


STUDENT_ID_NUMBER = 20190258  # You MUST assign your 8-digit student ID number.


def robot_control(hubo):
    ### START OF CODE SPACE ###

    # helper functions
    def turn_right(hubo):
        for _ in range(3): hubo.turn_left()

    def turn_opp(hubo):
        for _ in range(2): hubo.turn_left() 
    
    def go_straigt_n(hubo, n):
        for _ in range(n): hubo.move()
    
    def drop_beeper_n(hubo, n):
        for _ in range(n): hubo.drop_beeper()
    
    def command(hubo, comm):
        mapping = {'north': 1,
                   'west' : 2,
                   'south': 3,
                   'east' : 4,
                   'jump' : 5
                  }
        drop_beeper_n(hubo, mapping[comm])
    
    def place_jump_and_jump(hubo):
        command(hubo, 'jump')
        turn_opp(hubo)
        hubo.move()
        turn_opp(hubo)
        hubo.move()

    # main routine
    def place_commands(hubo):
        hubo.move()
        command(hubo, 'west') # (10, 8)
        turn_opp(hubo)
        go_straigt_n(hubo, 5)
        command(hubo, 'south') # (5, 8)
        hubo.turn_left()
        hubo.move()
        command(hubo, 'jump') # (5, 7)
        turn_right(hubo)
        go_straigt_n(hubo, 2)
        hubo.turn_left()
        go_straigt_n(hubo, 3)

        place_jump_and_jump(hubo) # (3, 4)
        hubo.turn_left()
        go_straigt_n(hubo, 2)
        place_jump_and_jump(hubo) # (5, 3)

        hubo.move()
        hubo.turn_left()
        go_straigt_n(hubo, 2)
        hubo.turn_left()
        go_straigt_n(hubo, 2)
        hubo.turn_left()
        hubo.move()
        command(hubo, 'jump') # (5, 4)
        turn_opp(hubo)
        hubo.move()
        turn_right(hubo)
        go_straigt_n(hubo, 2)
        hubo.turn_left()

        place_jump_and_jump(hubo) # (7, 5)
        hubo.turn_left()
        go_straigt_n(hubo, 2)
        command(hubo, 'jump') # (5, 6)

    place_commands(hubo)

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
