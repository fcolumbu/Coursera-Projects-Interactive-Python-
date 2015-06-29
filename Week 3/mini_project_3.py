# template for "Stopwatch: The Game"
import simplegui

# define global variables
canvas_width = 350
canvas_height = 200
control_width = 150
tick_count = 0      # sequential count of 100 msec ticks
stop_count = 0      # number of times the stop button is pressed
hit_count = 0       # number of times stop occurs on a whole second  
score = '0 / 0'     # successes / attempts

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format():
    global tick_count
    seconds_and_tenths = tick_count % 600
    num_seconds_and_tenths = seconds_and_tenths
    seconds_and_tenths = str(seconds_and_tenths)
    if (num_seconds_and_tenths < 10):
        seconds_and_tenths = "00." + seconds_and_tenths
    elif (num_seconds_and_tenths < 100):
        seconds_and_tenths = "0" + seconds_and_tenths[0] + '.' + seconds_and_tenths[1]
    else:
        seconds_and_tenths = seconds_and_tenths[:2] + '.' + seconds_and_tenths[2]
    minutes = tick_count // 600
    current_time = str(minutes) + ':' + seconds_and_tenths
    return(current_time)

def get_score():
    global score
    return(score)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()

def stop():
    global tick_count
    global stop_count
    global hit_count
    global score
    if (timer.is_running() and (tick_count % 10 == 0)):
        timer.stop()    # Successful stop on whole second
        stop_count += 1
        hit_count += 1
#        print 'Stop = ', stop_count
#        print 'Hit = ', hit_count
        score = str(hit_count) + ' / '+ str(stop_count) 
        return()
    elif (timer.is_running() and (tick_count % 10 != 0)):
        timer.stop()    # Unsuccessful stop
        stop_count += 1
#        print 'Stop = ', stop_count
#        print 'Hit = ', hit_count
        score = str(hit_count) + ' / '+ str(stop_count)
        return()
    else:               # repeated press of the stop button
        return()
 

def reset():
    global tick_count
    global stop_count
    global hit_count
    global score
    stop_count = 0
    hit_count = 0 
    tick_count = 0
    score = '0 / 0'
    timer.stop()

    
    
# define event handler for timer with 0.1 sec interval

def tick():
    global tick_count
    tick_count += 1
    
# define draw handler

def draw_handler(canvas):
    global tick_count
    canvas.draw_text(format(), (80, 120), 56, 'Red', 'sans-serif')
    canvas.draw_text(get_score(), (275, 50), 22, 'Green', 'sans-serif')

    # create frame
frame = simplegui.create_frame('Stopwatch: The Game', canvas_width,canvas_height, control_width)

# register event handlers
button1 = frame.add_button('Start', start, 100)
button2 = frame.add_button('Stop', stop, 100)
button3 = frame.add_button('Reset', reset, 100)
timer = simplegui.create_timer(100, tick)
frame.set_draw_handler(draw_handler)
# start frame
frame.start()


