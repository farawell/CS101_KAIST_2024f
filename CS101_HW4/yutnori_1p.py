import time
import random
from cs1graphics import *
from hidden import get_piece_image, create_boards, create_yut_sticks, throw_yut_sticks, add_turn_text, add_throw_button_and_wait, clear_yut_stick_board


class Piece:
    def __init__(self, piece_id, start_index):
        """
        Task 1.1.
            Initialize the following attributes of `Piece` class.
                piece_id (int)
                start_index (int)
                current_index (int)
        
        Input
            piece_id (int): id of the piece
            start_index (int): start index of the piece which is one of -1, -2, -3, -4.
        Output
            None
        """
        ##### Implement Here #####
        if start_index not in range(-4, 0):
            raise ValueError("start_index should be among -1, -2, -3 and -4")
        
        if not isinstance(piece_id, int) or not isinstance(start_index, int):
            raise ValueError("Both piece_id and start_index should be integer")

        self.piece_id = piece_id
        self.start_index = start_index
        self.current_index = start_index
        ##########################
        
    def get_point_by_current_index(self):
        """
        Task 1.2.
            Return the x and y coordinates where the piece should be located in the canvas.
            Refer to the figures that describe the correnpondence between indices and points.
        
        Output
            x, y (tuple of int): x and y coordinates where the piece should be located in the canvas
        """
        ##### Implement Here #####
        idx = self.current_index

        if idx == -1: return (480, 250)
        elif idx == -2: return (520, 250)
        elif idx == -3: return (480, 350)
        elif idx == -4: return (520, 350)

        if 1 <= idx <= 30:
            pos_arr = [
                (350, 290), (350, 230), (350, 170), (350, 110), (350, 50), (290,50),
                (230, 50), (170, 50), (110, 50), (50, 50), (50, 110), (50, 170),
                (50, 230), (50, 290), (50, 350), (110, 350), (170, 350), (230, 350),
                (290, 350), (350, 350), (300, 100), (250, 150), (200, 200), (150, 250),
                (100, 300), (100, 100), (150, 150), (200, 200), (250, 250), (300, 300)
            ]
            return pos_arr[idx - 1]
        else:
            print("[get_point_by_current_index()]: Wrong current_index\n")
            return -1
        ##########################
        
    def set_current_index(self, steps_to_move):
        """
        Task 1.3.
            Change the attribute `current_index` based on the movement rules.
        
        Input
            steps_to_move (int): number of steps to move by Yut sticks in this turn
        Output
            None
        """
        ##### Implement Here #####
        if steps_to_move <= 0 or not isinstance(steps_to_move, int): return

        i = steps_to_move
        # Landed on the dark points in the previous step
        if self.current_index in range(-4, 0):
            self.current_index = 1
            i -= 1
        elif self.current_index in [5, 10, 15, 23, 28]:
            if self.current_index in [5, 10]:
                self.current_index += 16 # Path choosing
            elif self.current_index in [23, 28]:
                self.current_index = 29 # Path choosing
            elif self.current_index == 15:
                self.current_index += 1 # Path choosing
            i -= 1

        # Traverse normally, handling edge cases
        while i != 0:
            if self.current_index == 20:
                self.current_index = 0
                break
            elif self.current_index == 30:
                self.current_index = 20
            elif self.current_index == 25:
                self.current_index = 15
            else: 
                self.current_index += 1
            i -= 1
        
        return
        ##########################


class Player:
    def __init__(self, player_id, start_index):
        self.player_id = player_id
        self.piece = Piece(piece_id=0, start_index=start_index)
    
    def move_piece_by_yut_sticks(self, yut_sticks):
        """
        Task 1.4.
            (1) Calculate the number of steps to move using `yut_sticks`.
            (2) Move the player's piece by the number of steps.
        
        Input:
            yut_sticks (list of str): list of 4 strings each of which is either "marked" or "unmarked".
        Output:
            None
        """
        ##### Implement Here #####
        yut_move_dict = {
            3: 1, # Do
            2: 2, # Gae
            1: 3, # Geol
            0: 4, # Yut
            4: 5  # Mo
        }
        marked_side_num = yut_sticks.count("marked")
        steps_to_move = yut_move_dict[marked_side_num]
        self.piece.set_current_index(steps_to_move)
        ##########################

    def is_winner(self):
        """
        Task 1.5.
            Determine whether the player is currently the winner.
            A player is the winner if every piece of the player currently completes a full round on the Yut board.
        
        Output
            is_player_winner (bool): whether the player is the current winner
        """
        ##### Implement Here #####
        return self.piece.current_index == 0
        ##########################


def create_piece_images(canvas):
    piece_images = Layer()
    canvas.add(piece_images)
    return piece_images


def update_piece_images(piece_images, players):
    piece_images.clear()
    for player in players:
        if getattr(player.piece, "current_index", 0) == 0:
            continue
        piece_image = get_piece_image(player.player_id)
        x, y = player.piece.get_point_by_current_index()
        piece_image.moveTo(x, y)
        piece_images.add(piece_image)


def print_winner(player, yut_stick_board):
    winner_text = Text(f"Player {player.player_id} Win!")
    winner_text.setFontColor("white")
    winner_text.moveTo(0, -50)
    yut_stick_board.add(winner_text)
    

def expected_results():
    """ You can modify this function. """
    def print_attr(obj, attr):
        if hasattr(obj, attr):
            print(f"{attr}: {getattr(obj, attr)}")
            
    print("### Task 1.1 ###")
    piece = Piece(piece_id=0, start_index=-1)
    print_attr(piece, "piece_id")
    print_attr(piece, "start_index")
    print_attr(piece, "current_index")
    
    print("\n### Task 1.2 ###")
    piece.current_index = 15
    x, y = piece.get_point_by_current_index()
    print(f"Coordinates of the piece: {(x, y)}")
    
    print("\n### Task 1.3 ###")
    piece.set_current_index(steps_to_move=5)
    print_attr(piece, "current_index")
    
    print("\n### Task 1.4 ###")
    player = Player(player_id=0, start_index=-1)
    gae = ["marked", "unmarked", "marked", "unmarked"]
    player.move_piece_by_yut_sticks(yut_sticks=gae)
    print_attr(player.piece, "current_index")
    
    print("\n### Task 1.5 ###")
    player.piece.current_index = 20
    is_winner = player.is_winner()
    print(f"Is Player {player.player_id} the winner?: {is_winner}")
    do = ["marked", "unmarked", "marked", "marked"]
    player.move_piece_by_yut_sticks(yut_sticks=do)
    is_winner = player.is_winner()
    print(f"Is Player {player.player_id} the winner?: {is_winner}")
    

def play():
    """ Do not modify this function. """
    canvas = Canvas(600, 400, "grey", "Mini Yutnori")
    yut_stick_board = create_boards(canvas)
    yut_sticks = create_yut_sticks(yut_stick_board)
    
    start_index = random.randint(-4, -1)
    player = Player(player_id=0, start_index=start_index)
    piece_images = create_piece_images(canvas)
    update_piece_images(piece_images, [player])
    
    while True:
        turn_text = add_turn_text(player, yut_stick_board)
        throw_button = add_throw_button_and_wait(yut_stick_board)
        throw_yut_sticks(yut_sticks)
        
        moved = False
        while not moved:
            cue = canvas.wait() # wait indefinitely for user event
            click = cue.getMouseLocation()
            if 470 < click.getX() < 530 and 150 < click.getY() < 180:
                throw_yut_sticks(yut_sticks)
                continue
            if getattr(player.piece, "current_index", 0) == 0:
                continue
            if not isinstance(getattr(player.piece, "piece_id", None), int):
                continue
            x, y = player.piece.get_point_by_current_index()
            if click.distance(Point(x, y)) < 15:
                player.move_piece_by_yut_sticks([stick.face for stick in yut_sticks])
                moved = True
                
        if player.is_winner():
            break
        
        update_piece_images(piece_images, [player])
        clear_yut_stick_board(yut_stick_board, turn_text, throw_button)
    
    update_piece_images(piece_images, [player])
    clear_yut_stick_board(yut_stick_board, turn_text, throw_button)
    print_winner(player, yut_stick_board)


if __name__ == "__main__":
    expected_results()
    play()
