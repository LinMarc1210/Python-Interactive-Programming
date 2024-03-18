import simplegui
import random
import math

numrange = 100
secret = 0
current_guess = 0
remain_guess = 7

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret, numrange, remain_guess
    remain_guess = 7
    secret = random.randrange(0, numrange)
    print "New game, range is from 0 to", numrange
    print "Remaining Guesses:", remain_guess, "\n"


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global numrange
    numrange = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global numrange
    numrange = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    # call helper function
    global current_guess
    current_guess = int(guess)
    get_input(current_guess)
    if decrease_guess():
        print
        return
    print
        
        
# helper function
def get_input(guess):
    print "Current Guess:", guess
    if guess < 0 or guess >= numrange:
        print("Out of range")
    elif guess > secret:
        print("Lower!")
    elif guess < secret:
        print("Higher!")
    else:
        print("Correct! You win the game!")
    
def decrease_guess():
    global remain_guess
    remain_guess -= 1
    if remain_guess < 0:
        print("You lose... Start new game\n")
        new_game()
    else:
        print"Remaining Guesses:", remain_guess
        return 0

    
# create frame
frame = simplegui.create_frame("Guess Number", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0,100)", range100, 200)
frame.add_button("Range is [0,1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
