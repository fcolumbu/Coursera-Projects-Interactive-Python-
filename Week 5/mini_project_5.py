# implementation of card game - Memory
# http://www.codeskulptor.org/


import simplegui
import random
numbers1 = []
numbers = []
state = 0
turns = 0
exposed = []
first_card = 16
second_card = 16

           
# helper function to initialize globals
def new_game():
    global numbers, numbers1, exposed, state, turns
    exposed = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    numbers1 = range(8)
    numbers = range(8)
    random.shuffle(numbers1)	  # Three shuffles
    random.shuffle(numbers)       # Half deck / Half deck
    numbers = numbers + numbers1
    random.shuffle(numbers)       # Full deck
#    print numbers				  # Un-comment for testing
    state = 0
    turns = 0
    label.set_text("Turns = "+ str(turns))

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, exposed, first_card, second_card, turns
#    print state				  # Un-comment for testing
    if exposed[pos[0] / 50] == True:
        return
    if exposed[pos[0] / 50] == False:
        if state == 0:
            first_card = pos[0] / 50
            exposed[pos[0] / 50] = True

        elif state == 1: 
            second_card = pos[0] / 50 
            exposed[pos[0] / 50] = True
        else:        
            if (numbers[first_card] != numbers[second_card]): 
                exposed[first_card] = False
                exposed[second_card] = False
                state = 0
                turns += 1
                label.set_text("Turns = "+ str(turns))
                exposed[pos[0] / 50] = True
                first_card = pos[0] / 50
            else:
                state = 0
                turns += 1
                label.set_text("Turns = "+ str(turns))
                exposed[pos[0] / 50] = True
                first_card = pos[0] / 50
               
    state += 1
    if state == 3:
        state = 1

# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(16):
        canvas.draw_text(str(numbers[i]), ((50 * i + 4), 75), 76, 'White', "sans-serif")
        if exposed[i] is True:
            i += 1
        else:
            canvas.draw_line(((50 * i + 25), 0), ((50 * i + 25), 99), 48, 'Green')

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = " + str(turns))


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


