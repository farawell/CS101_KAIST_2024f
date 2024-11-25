################################################
# Author: Yohan Park (farawell777@kaist.ac.kr) #
################################################

balance = 0

def deposit(money) :
    # Input : (Integer) The amount of money that a user wants to deposit
    # Output : (None) No Output
    
    # Add the money to the current balance
    
    #################
    ### implement ###
    #################
    # Do something on here !
    global balance 
    balance += money
    print(f"You've deposited {money} won")
    #################

def withdrawal(money) :
    # Input : (Integer) The amount of money that a user wants to withdraw
    # Output : (None) No Output
    
    # Withdraw the money from the current balance

    #################
    ### implement ###
    #################
    # Do something on here !
    global balance
    if balance < money:
        print(f"You've withdrawn {money} won")
        print(f'But you only have {balance} won')
    else: 
        balance -= money
        print(f"You've withdrawn {money} won")
    #################


def bank() :
    # Input : (None) No Input
    # Output : (None) No Output
    
    while True:
        process = input("Deposit(d) or withdrawal(w) or balance check(c)? ")
        
        # If a user's input is empty string (''), then quit this function.
        # If a user's input is 'd', then ask the amount of money to deposit and deposit it.
        # If a user's input is 'w', then ask the amount of money to withdraw and withdraw it.
        # If a user's input is 'c', then check the current balance.

        #################
        ### implement ###
        #################
        # Do something on here !
        if process == '': return
        elif process == 'd':
            amount = input('How much do you want to deposit? ')
            deposit(int(amount))
        elif process == 'w':
            amount = input('How much do you want to withdraw? ')
            withdrawal(int(amount))
        elif process == 'c':
            print(f'Your current balance is {balance} won')
        else: print('Please, press d or w or return')
        #################

bank()
