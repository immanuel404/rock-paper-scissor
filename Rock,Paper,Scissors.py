### "Rock", "Paper", "Scissors", "Lizard", "Spock" ###
# By Emmanuel. O

import random

# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

def name_to_number(name):
    """convert name to number using if/elif/else"""
    if name == "rock":
        return 0
    elif name == "spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print "Name Not Found"
    # don't forget to return the result!
    
def number_to_name(number):
    """convert number to a name using if/elif/else"""
    if number == 0:
        return "rock"
    if number == 1:
        return "spock"
    if number == 2:
        return "paper"
    if number == 3:
        return "lizard"
    if number is 4:
        return "scissors"
    else:
        print "Number Not Found"
    # don't forget to return the result!    

def rpsls(player_choice): 
    # print a blank line to separate consecutive games
    print ""

    # print out the message for the player's choice
    print "Player Chooses ", player_choice

    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)

    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print "Computer Chooses ", comp_choice

    # compute difference of comp_number and player_number modulo five
    outcome = (comp_number - player_number) % 5
    print""
    print "Computing formula...outcome equals:", outcome

    # use if/elif/else to determine winner, print winner message
    if outcome == 0:
        print "Player and computer tie!"
    elif outcome <= 2:
        print "COMPUTER WINS!"
    else:
        print "PLAYER WINS!"
    return()
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("paper")

#rpsls("Spock")
#rpsls("paper")
#rpsls("lizard")
#rpsls("scissors")

# always remember to check your completed program against the grading rubric
