# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
init_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 3]  # pixels per tick
time = 0
score1 = 0
score2 = 0
paddle1_pos = HEIGHT / 2
paddle2_pos = HEIGHT / 2
paddle1_vel = 0
paddle2_vel = 0
key = ''

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists    draw(c)
    ball_pos = list(init_pos)
    if time %2 == 0:          # ball goes down on an even tick
        if direction == 'LEFT':
            ball_vel = [- random.randrange(3, 6), random.randrange(2, 6)]
        elif direction == 'RIGHT':
            ball_vel = [random.randrange(3, 6), random.randrange(2, 6)]
    else:                     # ball goes up on an even tick
        if direction == 'LEFT':
            ball_vel = [- random.randrange(3, 6), - random.randrange(2, 6)]
        elif direction == 'RIGHT':
            ball_vel = [random.randrange(3, 6), - random.randrange(2, 6)]
 
  
    
# define event handlers

def tick():
    """
       This prevents a "forever" game with paddles perfectly aligned.
    """   
    global time, ball_vel
    time = time + 1
    if ball_vel[0] > 0:
       ball_vel[0] += 5
    else:
       ball_vel[0] -= 5

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    paddle1_pos = HEIGHT / 2
    paddle2_pos = HEIGHT / 2
    paddle1_vel = 0
    paddle2_vel = 0
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    direction = ['RIGHT','LEFT']
    spawn_ball(direction[random.randrange(0,2)])

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel
    global HALF_PAD_HEIGHT, BALL_RADIUS, HEIGHT, WIDTH
    c.draw_text(str(score1), [140, 50], 36, 'Blue')
    c.draw_text(str(score2), [WIDTH - 160, 50], 36, 'Green')
    
    # collide and reflect off of top and bottom hand side of canvas
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= (HEIGHT - BALL_RADIUS):
        ball_vel[1] = - ball_vel[1] 

      
    # Check for ball hitting paddles
    # Left Paddle
    if ball_pos[0] <= BALL_RADIUS and abs(ball_pos[1] - paddle1_pos) <= PAD_HEIGHT - BALL_RADIUS:
        ball_vel[0] = - ball_vel[0]
        ball_vel[1] = - ball_vel[1]      
#        print ball_pos[1],"  ",abs(ball_pos[1] - paddle1_pos),' left rtn'
    elif ball_pos[0] <= BALL_RADIUS and abs(ball_pos[1] - paddle1_pos) > PAD_HEIGHT - BALL_RADIUS:
        spawn_ball('RIGHT')
        score2 += 1 
#        print 'RIGHT ', score2
 
     # Right Paddle
    if ball_pos[0] >= (WIDTH - BALL_RADIUS) and abs(ball_pos[1] - paddle2_pos) <= PAD_HEIGHT - BALL_RADIUS:
        ball_vel[0] = - ball_vel[0]
        ball_vel[1] = - ball_vel[1] 
#        print ball_pos[1],"  ",abs(ball_pos[1] - paddle2_pos),' right rtn'
    elif ball_pos[0] >= (WIDTH - BALL_RADIUS) and abs(ball_pos[1] - paddle2_pos) > PAD_HEIGHT - BALL_RADIUS:
        spawn_ball('LEFT')
        score1 += 1 
#        print 'LEFT ', score1
        
        
    # calculate ball position
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]  


    
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        

    # draw ball & update ball
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
   
    # draw paddles & update paddle's vertical position, keep paddle on the screen
  
    c.draw_line((HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT), (HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT), PAD_WIDTH, 'White') 
    c.draw_line((WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT), (WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT), PAD_WIDTH, 'White')    
    if  paddle1_pos <= HALF_PAD_HEIGHT:
        paddle1_vel = 0   # At the top
        paddle1_pos = HALF_PAD_HEIGHT 
    elif paddle1_pos >= HEIGHT - HALF_PAD_HEIGHT:
        paddle1_vel = 0   # At the bottom
        paddle1_pos = HEIGHT - HALF_PAD_HEIGHT
    else:
        paddle1_pos += paddle1_vel

    if  paddle2_pos <= HALF_PAD_HEIGHT:
        paddle2_vel = 0   # At the top
        paddle2_pos = HALF_PAD_HEIGHT 
    elif paddle2_pos >= HEIGHT - HALF_PAD_HEIGHT:
        paddle2_vel = 0   # At the bottom
        paddle2_pos = HEIGHT - HALF_PAD_HEIGHT
    else:
        paddle2_pos += paddle2_vel
    
    # draw scores
        
def keydown(key):
    acc = 5
    global paddle1_vel, paddle2_vel, paddle1_pos, paddle2_pos

    if  key == simplegui.KEY_MAP["w"] and paddle1_pos <= HALF_PAD_HEIGHT: # At the top
        paddle1_vel = 0
        paddle1_pos = HALF_PAD_HEIGHT

    elif key == simplegui.KEY_MAP["w"] and paddle1_pos > HALF_PAD_HEIGHT:
        paddle1_vel -= acc

    elif key == simplegui.KEY_MAP["s"] and paddle1_pos >= HEIGHT - HALF_PAD_HEIGHT: # At the bottom
        paddle1_vel = 0
        paddle1_pos = HEIGHT - HALF_PAD_HEIGHT
        
    elif key == simplegui.KEY_MAP["s"] and paddle1_pos < HEIGHT - HALF_PAD_HEIGHT:
        paddle1_vel += acc

    elif  key == simplegui.KEY_MAP["up"] and paddle2_pos <= HALF_PAD_HEIGHT: # At the top
        paddle2_vel = 0
        paddle2_pos = HALF_PAD_HEIGHT

    elif key == simplegui.KEY_MAP["up"] and paddle2_pos > HALF_PAD_HEIGHT:
        paddle2_vel -= acc

    elif key == simplegui.KEY_MAP["down"] and paddle2_pos >= HEIGHT - HALF_PAD_HEIGHT: # At the bottom
        paddle2_vel = 0
        paddle2_pos = HEIGHT - HALF_PAD_HEIGHT
        
    elif key == simplegui.KEY_MAP["down"] and paddle2_pos < HEIGHT - HALF_PAD_HEIGHT:
        paddle2_vel += acc

       
  
    
   
def keyup(key):
    global paddle1_vel, paddle2_vel, paddle1_pos, paddle2_pos
    if  key == simplegui.KEY_MAP["w"] and paddle1_pos <= HALF_PAD_HEIGHT: # At the top
        paddle1_vel = 0
        paddle1_pos = HALF_PAD_HEIGHT + 1
    elif key == simplegui.KEY_MAP["w"] and paddle1_pos != HALF_PAD_HEIGHT:
        paddle1_vel = 0

    elif key == simplegui.KEY_MAP["s"] and paddle1_pos >= HEIGHT - HALF_PAD_HEIGHT: # At the bottom
        paddle1_vel = 0
        paddle1_pos = HEIGHT - HALF_PAD_HEIGHT - 1
    elif key == simplegui.KEY_MAP["s"] and paddle1_pos != HEIGHT - HALF_PAD_HEIGHT:   
        paddle1_vel = 0
        
    if  key == simplegui.KEY_MAP["up"] and paddle2_pos <= HALF_PAD_HEIGHT: # At the top
        paddle2_vel = 0
        paddle2_pos = HALF_PAD_HEIGHT + 1
    elif key == simplegui.KEY_MAP["up"] and paddle2_pos != HALF_PAD_HEIGHT:
        paddle2_vel = 0

    elif key == simplegui.KEY_MAP["down"] and paddle2_pos >= HEIGHT - HALF_PAD_HEIGHT: # At the bottom
        paddle2_vel = 0
        paddle2_pos = HEIGHT - HALF_PAD_HEIGHT - 1
    elif key == simplegui.KEY_MAP["down"] and paddle2_pos != HEIGHT - HALF_PAD_HEIGHT:   
        paddle2_vel = 0        
        
       

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)
key = frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
timer = simplegui.create_timer(10000, tick)
button1 = frame.add_button('Restart', new_game)

# start frame
new_game()
frame.start()
timer.start()

