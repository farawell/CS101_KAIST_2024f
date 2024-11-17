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
    
    def place_two_jumps(hubo):
        command(hubo, 'jump')
        turn_opp(hubo)
        hubo.move()
        turn_opp(hubo)
        hubo.move()
        command(hubo, 'jump')
        hubo.move()
        command(hubo, 'jump')
        turn_opp(hubo)
        hubo.move()
    
    # main routine
    def place_commands(hubo):
        # place initial commands for minions
        hubo.move()
        command(hubo, 'jump')
        turn_opp(hubo)
        hubo.move()
        turn_opp(hubo)
        hubo.move()
        command(hubo, 'east')
        turn_right(hubo)
        go_straigt_n(hubo, 4)
        turn_right(hubo)
        command(hubo, 'south')
        go_straigt_n(hubo, 5)
        command(hubo, 'jump')

        # place first jump command in box2
        turn_right(hubo)
        go_straigt_n(hubo, 2)
        hubo.turn_left()
        hubo.move()
        hubo.turn_left()
        place_two_jumps(hubo)

        # place second jump command in box2
        hubo.turn_left()
        go_straigt_n(hubo, 2)
        hubo.turn_left()
        hubo.move()
        place_two_jumps(hubo)

        # place third jump command in box2
        turn_right(hubo)
        go_straigt_n(hubo, 4)
        turn_right(hubo)
        go_straigt_n(hubo, 5)
        turn_right(hubo)
        go_straigt_n(hubo, 3)
        turn_right(hubo)
        place_two_jumps(hubo)
    
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
