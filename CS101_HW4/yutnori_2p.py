from cs1graphics import *
from hidden import get_piece_image, create_boards, create_yut_sticks, throw_yut_sticks, add_turn_text, add_throw_button_and_wait, clear_yut_stick_board


class Piece:
    def __init__(self, piece_id, start_index):
        """
        Task 2.1.
            Initialize the following attributes of `Piece` class.
                piece_id (int)
                start_index (int)
                current_index (int)
                piggyback (bool)
        
        Input
            piece_id (int): id of the piece
            start_index (int): start index of the piece which is one of -1, -2, -3, -4.
        Output
            None
        """
        ##### Implement Here #####
        # From my code of Task 1
        if start_index not in range(-4, 0):
            raise ValueError("start_index should be among -1, -2, -3 and -4")
        if not isinstance(piece_id, int) or not isinstance(start_index, int):
            raise ValueError("Both piece_id and start_index should be integer")

        self.piece_id = piece_id
        self.start_index = start_index
        self.current_index = start_index
        self.piggyback = False
        ##########################

    def get_point_by_current_index(self):
        """
        Copy your previous code from Task 1.2.
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
        Copy your previous code from Task 1.3.
        """
        ##### Implement Here #####
        if steps_to_move <= 0 or not isinstance(steps_to_move, int): return
        i = steps_to_move
        
        # Landed on the dark points in the previous step
        if self.current_index in range(-4, 0):
            self.current_index = 1
            i -= 1
        elif self.current_index in [5, 10, 15, 23, 28]:
            # Path choosing
            if self.current_index in [5, 10]: self.current_index += 16
            elif self.current_index in [23, 28]: self.current_index = 29
            elif self.current_index == 15: self.current_index += 1
            i -= 1

        # Traverse normally, handling edge cases
        while i != 0:
            if self.current_index == 20:
                self.current_index = 0
                break
            elif self.current_index == 30: self.current_index = 20
            elif self.current_index == 25: self.current_index = 15
            else: self.current_index += 1
            i -= 1
        
        return
        ##########################


class Player:
    def __init__(self, player_id):
        self.player_id = player_id
        self.pieces = [
            Piece(piece_id=0, start_index=-2*player_id-1),
            Piece(piece_id=1, start_index=-2*player_id-2)
        ]
    
    def move_piece_by_yut_sticks(self, piece_id, yut_sticks):
        """
        Task 2.2.
            (1) Calculate the number of steps to move using `yut_sticks`.
            (2) Update a piece of the player corresponding to `piece_id` using `set_current_index`.
            (3) If the two pieces of the player land at the same point, set their 'piggyback' attributes to `True`.
        
        Input:
            piece_id (int): id of the piece to be moved
            yut_sticks (list of str): list of 4 strings each of which is either "marked" or "unmarked".
        Output:
            None
        """
        ##### Implement Here #####
        if piece_id not in [0, 1]:
            raise ValueError('piece_id should be either 0 or 1')

        # Part of the codes are from my previous code for Task 1
        yut_move_dict = {
            3: 1, # Do
            2: 2, # Gae
            1: 3, # Geol
            0: 4, # Yut
            4: 5  # Mo
        }
        marked_side_num = yut_sticks.count("marked")
        steps_to_move = yut_move_dict[marked_side_num]
        self.pieces[piece_id].set_current_index(steps_to_move) 

        if (self.pieces[0].current_index == self.pieces[1].current_index) \
            or (self.pieces[0].current_index in [23, 28] and self.pieces[1].current_index in [23, 28]):
            self.pieces[0].piggyback = True
            self.pieces[1].piggyback = True
        ##########################
    
    def is_winner(self):
        """
        Task 2.3.
            Determine whether the player is currently the winner.
            A player is the winner if every piece of the player currently completes a full round on the Yut board.
        
        Output
            is_player_winner (bool): whether the player is the current winner
        """
        ##### Implement Here #####
        return all([self.pieces[0].current_index == 0, self.pieces[1].current_index == 0])
        ##########################


def capture_and_get_next_players(current_player, current_opponent):
    """
    Task 2.4.
        (1) If one of the current player's pieces captures the opponent's pieces,
            update the captured pieces' attributes to set their `piggyback` attributes to `False`,
            and return them to their starting position.
        (2) This function should return a tuple of two Player objects:
            the next player and their opponent for the upcoming turn.
            If any pieces were captured, the turn remains the same.
    
    Input 
        current_player (Player): current player's object
        opponent_player (Player): the other player's object
    
    Output
        next_player, next_opponent (tuple of Player): the next player and its opponent player for the next iteration
    """
    ##### Implement Here #####
    captured = False
    
    # Check for all occurence of capture excluding the case for the index 0
    for piece in current_player.pieces:
        for opp_piece in current_opponent.pieces:
            on_same_loc = any([piece.current_index in [23, 28] and opp_piece.current_index in [23, 28], \
                               piece.current_index == opp_piece.current_index])
            if on_same_loc and opp_piece.current_index != 0:
                opp_piece.piggyback = False
                opp_piece.current_index = opp_piece.start_index
                captured = True

    if captured: return current_player, current_opponent
    else: return current_opponent, current_player
    ##########################


def create_piece_images(canvas):
    piece_images = Layer()
    canvas.add(piece_images)
    return piece_images


def update_piece_images(piece_images, players):
    piece_images.clear()
    for player in players:
        for piece in player.pieces:
            if getattr(piece, "current_index", 0) == 0:
                continue
            if not isinstance(getattr(piece, "piggyback", None), bool):
                continue
            piece_image = get_piece_image(player.player_id, piece.piggyback)
            x, y = piece.get_point_by_current_index()
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
            
    print("### Task 2.1 ###")
    piece = Piece(piece_id=0, start_index=-1)
    print_attr(piece, "piece_id")
    print_attr(piece, "start_index")
    print_attr(piece, "current_index")
    print_attr(piece, "piggyback")
    
    print("\n### Task 2.2 ###")
    player = Player(player_id=0)
    player.pieces[0].current_index = -1
    player.pieces[1].current_index = 2
    gae = ["marked", "unmarked", "marked", "unmarked"]
    player.move_piece_by_yut_sticks(piece_id=0, yut_sticks=gae)
    print_attr(player.pieces[0], "current_index")
    print_attr(player.pieces[0], "piggyback")
    print_attr(player.pieces[1], "piggyback")
    
    print("\n### Task 2.3 ###")
    player = Player(player_id=0)
    player.pieces[0].current_index = 0
    player.pieces[1].current_index = 20
    is_winner = player.is_winner()
    print(f"Is Player {player.player_id} the winner?: {is_winner}")
    do = ["marked", "unmarked", "marked", "marked"]
    player.move_piece_by_yut_sticks(piece_id=1, yut_sticks=do)
    is_winner = player.is_winner()
    print(f"Is Player {player.player_id} the winner?: {is_winner}")
    
    print("\n### Task 2.4 ###")
    player = Player(player_id=0)
    opponent = Player(player_id=1)
    player.pieces[0].current_index = 0
    player.pieces[1].current_index = 2
    opponent.pieces[0].current_index = 0
    opponent.pieces[1].current_index = 4
    
    gae = ["marked", "unmarked", "marked", "unmarked"]
    player.move_piece_by_yut_sticks(piece_id=1, yut_sticks=gae)
    next_player, next_opponent = capture_and_get_next_players(player, opponent)
    print(f"Captured piece goes to index {opponent.pieces[1].current_index}.")
    print(f"Next player is Player {next_player.player_id}.")
    print(f"Next opponent is Player {next_opponent.player_id}.")
    

def play():
    """ Do not modify this function. """
    canvas = Canvas(600, 400, "grey", "Mini Yutnori")
    yut_stick_board = create_boards(canvas)
    yut_sticks = create_yut_sticks(yut_stick_board)
    
    player, opponent = Player(player_id=0), Player(player_id=1)
    piece_images = create_piece_images(canvas)
    update_piece_images(piece_images, [player, opponent])
    
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
            for piece in player.pieces:
                if getattr(piece, "current_index", 0) == 0:
                    continue
                if not isinstance(getattr(piece, "piece_id", None), int):
                    continue
                x, y = piece.get_point_by_current_index()
                if click.distance(Point(x, y)) < 15:
                    player.move_piece_by_yut_sticks(piece.piece_id, [stick.face for stick in yut_sticks])
                    moved = True
                
        if player.is_winner():
            break
        
        player, opponent = capture_and_get_next_players(player, opponent)
        update_piece_images(piece_images, [player, opponent])
        clear_yut_stick_board(yut_stick_board, turn_text, throw_button)
    
    update_piece_images(piece_images, [player, opponent])
    clear_yut_stick_board(yut_stick_board, turn_text, throw_button)
    print_winner(player, yut_stick_board)


if __name__ == "__main__":
    expected_results()
    play()
