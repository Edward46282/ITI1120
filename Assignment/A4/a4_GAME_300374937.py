# In this implementation a card (that is not a 10) is represented
# by a 2 character string, where the 1st character represents a rank and the 2nd a suit.
# Each card of rank 10 is represented as a 3 character string, first two are the rank and the 3rd is a suit.

import random

def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
         input("\nPress enter to continue. ")
         print()
    except SyntaxError:
         pass


def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663') # remove a queen as the game requires
    return deck

def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    random.shuffle(deck)

#####################################

def deal_cards(deck):
     '''(list of str)-> tuple of (list of str,list of str)

     Returns two lists representing two decks that are obtained
     after the dealer deals the cards from the given deck.
     The first list represents dealer's i.e. computer's deck
     and the second represents the other player's i.e user's list.
     '''
     dealer=[]
     other=[]

     # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
     # YOUR CODE GOES HERE
     number_of_loop = 0
     while number_of_loop < len(deck):
         if number_of_loop == 1 or number_of_loop % 2 != 0:
             dealer.append(deck[number_of_loop])
         elif number_of_loop % 2 == 0 or number_of_loop == 0:
             other.append(deck[number_of_loop])
         number_of_loop += 1


     return (dealer, other)
 


def remove_pairs(l):
    '''
     (list of str)->list of str

     Returns a copy of list l where all the pairs from l are removed AND
     the elements of the new list shuffled

     Precondition: elements of l are cards represented as strings described above

     Testing:
     Note that for the individual calls below, the function should
     return the displayed list but not necessarily in the order given in the examples.

     >>> remove_pairs(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    no_pairs=[]

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE
    to_remove = []
    coeff = []
    l.sort()
    for card in l:
        x = card[0]
        coeff += x

    coeff.sort()
    
    for i in range(0,len(l)-1,2):
        if coeff[i] == coeff[i+1]:
            to_remove.append(l[i])
            to_remove.append(l[i+1])

    no_pairs = l
    
    for dup in to_remove:
        no_pairs.remove(dup) 
    

    random.shuffle(no_pairs)
    return no_pairs


def print_deck(deck):
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE
    updated_deck = " ".join(deck)
    print(updated_deck)

    
def get_valid_input(n):
     '''
     (int)->int
     Returns an integer given by the user that is at least 1 and at most n.
     Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]
     
     Precondition: n>=1
     '''

     # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
     # YOUR CODE GOES HERE
     user_input = int(input("I have " + str(n) +" cards. If 1 stands for my first card and\n" + str(n) + " for my last card, which of my cards would you like?\nGive me an integer between 1 and "+ str(n)+": "))
     if user_input >= 1 and user_input <= n:
         return user_input
     elif user_input < 1 or user_input > n:
         user_input = int(input("Invalid number. Please enter integer between 1 and "+str(n)+":\t"))
         while user_input < 1 or user_input > n:
             user_input = int(input("Invalid number. Please enter integer between 1 and "+str(n)+":\t"))
         return user_input


def play_game():
     '''()->None
     This function plays the game'''
    
     deck=make_deck()
     shuffle_deck(deck)
     tmp=deal_cards(deck)

     dealer=tmp[0]
     human=tmp[1]

     print("Hello. My name is Robot and I am the dealer.")
     print("Welcome to my card game!")
     print("Your current deck of cards is:")
     print_deck(human)
     print("Do not worry. I cannot see the order of your cards")

     print("Now discard all the pairs from your deck. I will do the same.")
     wait_for_player()
     
     dealer=remove_pairs(dealer)
     human=remove_pairs(human)

     # COMPLETE THE play_game function HERE
     # YOUR CODE GOES HERE
     ending_message = " "
     while len(human) != 0 and len(dealer) != 0:
         print("***********************************************************")
         print("Your turn.\n\nYour current deck of cards is:\n\n")
         print_deck(human)
         remove_pairs(dealer)
         user_input = get_valid_input(len(dealer))
         if user_input == 1:
             print("\nYou asked for my " + str(user_input) + "st card.")
         elif user_input == 2:
             print("\nYou asked for my " + str(user_input) + "nd card.")
         elif user_input == 3:
             print("\nYou asked for my " + str(user_input) + "rd card.")
         else:
             print("\nYou asked for my " + str(user_input) + "th card.")

         print("Here it is. It is " + dealer[user_input-1])
         human.append(dealer[user_input-1])
         
         print("\nWith "+dealer[user_input-1]+" added, my current deck of card is:\n\n")
         dealer.pop(user_input-1)
         print_deck(human)
         print("\nAnd after discarding pairs and shuffling, your deck is:\n")
         remove_pairs(human)
         print_deck(human)
         if len(dealer) == 0:
             print("***********************************************************")
             print("Ups. I do not have any more cards\nYou lost! I, Robot, Win")
             return ending_message
         wait_for_player()
         print("***********************************************************")
         robot_pick = random.randint(1,len(human))
         if robot_pick == 1:
             print("\nI took your " + str(robot_pick) + "st card.")
         elif robot_pick == 2:
             print("\nI took your " + str(robot_pick) + "nd card.")
         elif robot_pick == 3:
             print("\nI took your " + str(robot_pick) + "rd card.")
         else:
             print("\nI took your " + str(robot_pick) + "th card.")
         dealer.append(human[robot_pick-1])
         human.pop(robot_pick-1)
         remove_pairs(dealer)
         wait_for_player()

     if len(dealer) == 0:
        print("***********************************************************")
        print( "Ups. I do not have any more cards\nYou lost! I, Robot, Win")
     elif len(human) == 0:
        print("***********************************************************")
        print("Ups. You do not have any more cards\nCongraduations! You, Human, win")
         
        
	
	 

# main
play_game()
