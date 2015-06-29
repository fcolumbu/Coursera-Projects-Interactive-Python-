# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random


# initialize global variables used in your code
canvas_width = 350
canvas_height = 200
control_width = 150
secret_number = 0
user_guess = 0
game_range = 100
guess_number = 0

# helper function to start and restart the game
def new_game():
    global secret_number
    global game_range
    global guess_number
    secret_number = random.randrange(0, game_range)
    guess_number = 0
    
    return
    
# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global game_range
    game_range = 100
    # Prefill the text box with the high end of the range.
    inp.set_text(game_range)
    new_game()
    return

def range1000():
    # button that changes range to range [0,1000) and restarts
    global game_range    
    game_range = 1000
    # Prefill the text box with the high end of the range.
    inp.set_text(game_range) 
    new_game()
    return
    
def input_guess(guess):
    # main game logic goes here	
    global secret_number
    global guess_number
    guess_number += 1 # Track the number of guesses.
    
#    print secret_number # This line is for debugging.
    print guess
    print "Try number: ", guess_number
    
    if not guess.isdigit():
        print "Input integers only.\n"
        if (game_range == 100 and guess_number == 7):
            print "Game Over :(\nTry again - You are set for [0, 100)"
            range100()
            return(0)
        elif (game_range == 1000 and guess_number == 10):
            print "Game Over :(\nTry again - You are set for [0, 1000)"
            range1000()
            return(0)
        else:
            return(0)
    guess = int(guess)
    if (secret_number > guess):
        print "Higher\n"
    elif (secret_number < guess):
        print "Lower\n"
    else:
        print "Correct\nGo ahead, play again!\n"
        if game_range == 100:
            range100()
        else:
            range1000()
    if (game_range == 100 and guess_number == 7):
        print "Game Over :(\nTry again - You are set for [0, 100)\n"
        range100()
    elif (game_range == 1000 and guess_number == 10):
        print "Game Over :(\nTry again - You are set for [0, 1000)\n"
        range1000()
        
    return(int(guess))
    
    
def main():
    new_game()
    
main()    


# create frame
frame = simplegui.create_frame('Guess the number', canvas_width,canvas_height, control_width)


# register event handlers for control elements

button1 = frame.add_button('[0, 100)', range100, 100)
button2 = frame.add_button('[0, 1000)', range1000, 100)
inp = frame.add_input('Guess the number:', input_guess, 100)

# Prefill the text box with the high end of the range.
inp.set_text('100')

# call new_game and start frame
frame.start()

