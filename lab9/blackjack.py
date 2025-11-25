import random
from cs1graphics import *

img_path = './images/'

suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
face_names = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
value = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



bj_board = Canvas(600, 400, 'dark green', 'Black Jack 101')


"""
Define the Card class
"""



def create_deck(number = 1):
    """
    Create a list("deck") of all 52 cards, shuffle them and return the list.
    The list 'deck' have to include Card objects
    A Card is represented by a object with four attributes: the face, the suit, value, state, and the image object
    First, Have to define class 'Card'
    """





def hand_value(hand):
    """
    hand is a list including card objects
    Compute the value of the cards in the list "hand"
    """





def card_string(card):
    """
    Parameter "card" is a Card object
    Return a nice string to represent a card
    (sucn as "a King of Spades" or "an Ace of Diamonds")
    """


def draw_card(dealer,player):
    """
    This funuction add the cards of dealer and player to canvas, bj_board.
    If the state of each Card object is false, then you have to show the hidden card image(Back.png).
	The dealer's first card is hidden state.
    The parameter dealer and player are List objects including Card Objects.

    The start position of dealer's card is (100,100).
    The start position of player's card is (100,300).

    You can use the following methods for positioning images and text:
    Image() Object, Text() Object, moveTo() method, setDepth() method.

    You should use help function -
    help('cs1graphics.Image') -> about Image(), moveTo(), setDepth()
    help('cs1graphics.Text') -> about Text(),moveTo(), setDepth()
    """
    depth = 100
    x0,y0 = 100,100
    x1,y1 = 100,300

    bj_board.clear()


def ask_yesno(prompt):
    while True:
        answer = input(prompt)
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("I beg your pardon!")




def main():

    deck = []

    while True:
        # prompt for starting a new game and create a deck
        print ("Welcome to Black Jack 101!\n")
        if len(deck) < 12:
            deck = create_deck()

    # create two hands of dealer and player
        dealer = []
        player = []

    # initial two dealings
        card = deck.pop()
        print ("You are dealt " + card_string(card))
        player.append(card)

        card = deck.pop()
        print ("Dealer is dealt a hidden card")
        card.state=False
        dealer.append(card)

        card = deck.pop()
        print ("You are dealt " + card_string(card))
        player.append(card)

        card = deck.pop()
        print ("Dealer is dealt " + card_string(card))
        dealer.append(card)

        print ("Your total is", hand_value(player))
        draw_card(dealer,player)


    # player's turn to draw cards
        while hand_value(player) < 21 and ask_yesno("Would you like another card? (y/n) "):
        # draw a card for the player
            card = deck.pop()
            print ("You are dealt " + card_string(card))
            player.append(card)
            print ("Your total is", hand_value(player))

            draw_card(dealer,player)
    # if the player's score is over 21, the player loses immediately.
        if hand_value(player) > 21:
            print ("You went over 21! You lost.")
            dealer[0].state = True
            draw_card(dealer,player)
        else:
        # draw cards for the dealer while the dealer's score is less than 17
            print ("\nThe dealer's hidden card was " + card_string(dealer[0]))
            while hand_value(dealer) < 17:
                card = deck.pop()
                print ("Dealer is dealt " + card_string(card))
                dealer.append(card)
                print ("The dealer's total is", hand_value(dealer))

            dealer[0].state = True
            draw_card(dealer,player)
        # summary
            player_total = hand_value(player)
            dealer_total = hand_value(dealer)
            print ("\nYour total is", player_total)
            print ("The dealer's total is", dealer_total)

            if dealer_total > 21:
                print ("The dealer went over 21! You win!")
            else:
                if player_total > dealer_total:
                    print ("You win!")
                elif player_total < dealer_total:
                    print ("You lost!")
                else:
                    print ("You have a tie!")

        if not ask_yesno("\nPlay another round? (y/n) "):
            bj_board.close()
            break





main()
