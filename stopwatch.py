# template for "Stopwatch: The Game"

import simplegui
# define global variables
time = 0
trial = 0
good = 0
running = False
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    ms = t%10
    minute = int(t/600)
    second = int((t%600)/10)
    if t == 0:
        return '0:00.0'
    elif second >= 10:
        return str(minute)+':'+str(second)+'.'+str(ms)
    else:
        return str(minute)+':0'+str(second)+'.'+str(ms)
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global timer
    timer.start()

def stop():
    global timer, trial, good, time, running
    running = timer.is_running()
    if running:
        trial += 1	
        if time%10 == 0:
            good += 1
    timer.stop()

def reset():
    global time, trial, good
    time, trial, good = 0, 0, 0
    timer.stop()
    

# define event handler for timer with 0.1 sec interval
def increment():
    global time
    time += 1

timer = simplegui.create_timer(100, increment)

# define draw handler
def draw(canvas):
    global time, trial, good
    canvas.draw_text(format(time),[50, 75], 24, "White")
    canvas.draw_text(str(good)+'/'+str(trial),[75, 24], 24, "Green")

    
# create frame
frame = simplegui.create_frame("Stopwatch", 150, 150)
frame.add_button("Start", start, 150)
frame.add_button("Stop", stop, 150)
frame.add_button("Reset", reset, 150)

# register event handlers
frame.set_draw_handler(draw)

# start frame
frame.start()

# Please remember to review the grading rubric
