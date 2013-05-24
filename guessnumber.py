# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import simplegui
import math
# initialize global variables used in your code
secret = 0
myguess = 0
num_range = 100
count = 0
maxcount = 0
# define event handlers for control panel

def init():
    global num_range, count, maxcount, secret
    count = 0
    secret = random.randrange(0, num_range)
    maxcount = math.ceil(math.log(num_range)/math.log(2))
    print 'New game. Range is frome 0 to', num_range
    print 'Number of remaining guesses is', maxcount
    print 'True value: ' , secret, '\n'
    
def range100():
    # button that changes range to range [0,100) and restarts
    global num_range
    num_range = 100
    init()    
    
def range1000():
    # button that changes range to range [0,1000) and restarts
    global num_range
    num_range = 1000
    init()
  
def get_input(guess):
    # main game logic goes here	
    global secret, count, maxcount
    count += 1
    myguess = int(guess)
    if myguess == secret:
        print 'Guess was', myguess
        print 'Number of remaining guesses is', maxcount - count
        print 'Correct! \n'
        init()
    elif myguess > secret:
        print 'Guess was', myguess
        print 'Number of remaining guesses is', maxcount - count
        print 'Lower!', '\n'
    else:
        print 'Guess was', myguess
        print 'Number of remaining guesses is', maxcount - count
        print 'Higher', '\n'
    if count == maxcount:
        print 'You lose! No more trial! \n'
        init()

# create frame
frame = simplegui.create_frame("Guess the number", 300, 300)

# register event handlers for control elements
b100 = frame.add_button("Range: 0 - 100", range100, 200)
b1000 = frame.add_button("Range: 0 - 1000", range1000, 200)
inp = frame.add_input("My guess", get_input, 200)

init()
# start frame
frame.start()


# always remember to check your completed program against the grading rubric
