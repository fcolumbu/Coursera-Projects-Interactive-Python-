# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def number_to_name(number):
    # fill in your code below
    if (number == 0):
        name = 'rock'
    elif (number == 1):
        name = 'Spock'
    elif (number == 2):
        name = 'paper'
    elif (number == 3):
        name = 'lizard'        
    elif (number == 4):
        name = 'scissors'
    else:
        name = 'Error'
    return (name)
        
    # convert number to a name using if/elif/else
    # don't forget to return the result!

    
def name_to_number(name):
    # fill in your code below
    if (name == 'rock'):
        number = 0
    elif (name == 'Spock'):
        number = 1
    elif (name == 'paper'):
        number = 2
    elif (name == 'lizard'):
        number = 3
    elif (name == 'scissors'):
        number = 4
    else:
        number = 999 # Error code
    return (number)
      
    # convert name to number using if/elif/else
    # don't forget to return the result!


def rpsls(name): 
    # fill in your code below
    import random
    # convert name to player_number using name_to_number
    player_number = name_to_number(name)
    # compute random guess for comp_number using random.randrange()
    computer_number = random.randrange(0, 5)
    print ('Player chooses ' + name)
    
    # convert comp_number to name using number_to_name
    print ('Computer chooses ' + str(number_to_name(computer_number)))    
    # compute difference of player_number and comp_number modulo five
    difference = (player_number - computer_number) % 5
    
    # use if/elif/else to determine winner
    if (difference == 1 or difference == 2):
        print ('Player wins!')
    elif (difference == 3 or difference == 4):
        print ('Computer wins!')
    else:
        print ('Player and computer tie!')
       
    # print results
    print ('\n')
    
# test your code <- These are "Player" inputs.
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")




