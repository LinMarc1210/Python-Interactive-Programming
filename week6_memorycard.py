# implementation of card game - Memory
import simplegui
import random

WIDTH = 800
HEIGHT = 100
SPACE = WIDTH / 16

deck = []
exposed = [False] * 16
state = 0   # 同時有幾張翻開
turns = 0
first_idx = 0
second_idx = 0

# helper function to initialize globals
# 設置初始值
def new_game():
    global deck, exposed, state, turns
    lst1 = range(8)
    lst2 = range(8)
    lst1.extend(lst2)
    deck = lst1
    random.shuffle(deck)
    exposed = [False] * 16
    state = 0
    turns = 0
    label.set_text("Turns = " + str(turns))

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed, state, turns, first_idx, second_idx
    x = pos[0] / 50
    if exposed[x] == True:
        pass
    elif state == 0:
        turns += 1
        state = 1
        first_idx = x
    elif state == 1:
        state = 2
        second_idx = x
    else:
        state = 1
        turns += 1
        if deck[first_idx] == deck[second_idx]:
            exposed[first_idx], exposed[second_idx] = True, True
        else:
            exposed[first_idx], exposed[second_idx] = False, False
        first_idx = x
        
    exposed[x] = True
    label.set_text("Turns = " + str(turns))
    
    
                        
# cards are logically 50x100 pixels in size
# 畫卡片
def draw(canvas):
    index = 0
    for num in deck:
        canvas.draw_text(str(num), [15+SPACE*index, HEIGHT/2+10], 36, "White")
        if exposed[index] == False:
            canvas.draw_line([SPACE*index+25, 0],[SPACE*index+25, 100], 50, "Green")
            canvas.draw_line([SPACE*index, 0],[SPACE*index, 100], 1, "Black")
        index += 1
        
        
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")
label.set_text("Turns = " + str(turns))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric