from cs1graphics import *
import time
import random
import copy

canvas = Canvas(640, 580)
canvas.setTitle("Memento")

path = "./images/"
names = ("Cho\'Gath.png", "Ahri.png", "Jinx.png", 
         "Lulu.png", "Nidalee.png", "Teemo.png")
cards = []
num_pads = []
tries = 1
correct_list = []

def initialize():
    # initialize cards
    for i in range(6):
        for k in range(4):
            img = Image(path+names[i])
            temp_tuple = (img, names[i])
            cards.append(temp_tuple)

    for i in range(24):
        card = Layer()
        rect = Rectangle(90, 120, Point(0, 0))
        text = Text(str(i), 18, Point(0, 0))
        card.add(rect)
        card.add(text)
        num_pads.append(card)

    ################################################################
    # 3-2-1. shuffle the card list
    ################################################################
    random.shuffle(cards)

def print_cards():
    canvas.clear()
    w = 0
    h = 0
    i_w = 70
    i_h = 90
    for i in range(len(num_pads)):
        ################################################################
        if i in correct_list:   
        ################################################################
            cards[i][0].moveTo(i_w + w, i_h+h)
            canvas.add(cards[i][0])
        else:
            num_pads[i].moveTo(i_w + w, i_h+h)
            canvas.add(num_pads[i])

        w += 100
        if w % 600 == 0:
            w = 0
            h += 130
    time.sleep(1)


def is_valid(num1, num2):
    ###########################################################################
    # 3-1-1. Check if any of two numbers exists in the current correct list,
    #        two numbers are the same,
    #        or both of the numbers are within a valid range.
    # Return Boolean value according to the result.
    ###########################################################################
    not_exist = not any(num in correct_list for num in [num1, num2])
    are_different = (num1 != num2)
    in_range = all(0 <= num <= 23 for num in [num1, num2])

    return (not_exist and are_different and in_range)


def check(num1, num2):
    ###########################################################################
    # 3-1-2. At first, visualize the screen including the two cards
    #        (num1-th card and num2-th card).
    #        If two pictures of the two cards are same,
    #        put two numbers into the correct list.
    #        If not, re-visualize the original screen.
    # Return Boolean value according to the result.
    ###########################################################################
    global correct_list
    correct_list_backup = copy.deepcopy(correct_list)
    correct_list.extend([num1, num2])
    print_cards()

    are_same_cards = (cards[num1][1] == cards[num2][1])

    if are_same_cards:
        correct_list_backup.extend([num1, num2])
        correct_list = copy.deepcopy(correct_list_backup)
        print_cards()
        return True
    else:
        correct_list = copy.deepcopy(correct_list_backup)
        print_cards()
        return False

initialize()
for i in range(24):
    correct_list.append(i)
print_cards()
time.sleep(3)
correct_list = []
print_cards()
print("### Welcome to the Python Memento game!!! ###")
###############################################################################
while len(correct_list) < 24: # 3-2-2. Rewrite the condition for termination
###############################################################################
    ###########################################################################
    # 3-2-3. Print the number of tries and the corrected pairs
    if tries == 1: numeral = 'st'
    elif tries == 2: numeral = 'nd'
    elif tries == 3: numeral = 'rd'
    else: numeral = 'th'
    
    print(str(tries) + numeral +" try. You got " + str(len(correct_list)//2) + " pairs.")
    # print(str(tries) + "th try. You got " + str(len(correct_list)//2) + " pairs.")
    ###########################################################################
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    if not is_valid(num1, num2):
        print()
        continue

    if check(num1, num2):
        print("Correct!", end = '\n\n')
    else:
        print("Wrong!", end = '\n\n')
    ###########################################################################
    # 3-2-4. Update number of tries (global variable, tries)
    ###########################################################################
    tries += 1