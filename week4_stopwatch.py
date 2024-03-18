# template for "Stopwatch: The Game"
import simplegui

# define global variables
time = 0
click = 0
success = 0

# define helper function format that converts time
def format(t):
    tt = t
    display = ""
    display = str(tt / 600) + ":"
    tt %= 600
    display = display + str(tt / 100)
    tt %= 100
    display = display + str(tt / 10) + "." + str(tt % 10)
    return display
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def Start():
    timer.start()
    
def Stop():
    global click, success
    if timer.is_running():
        click += 1
        if time % 10 == 0:
            success += 1
    timer.stop()
    
def Reset():
    global time, click, success
    time = click = success = 0
    
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time
    time += 1

# define draw handler
def draw(canvas):
    suc_rate = str(success) + "/" + str(click)
    canvas.draw_text(format(time), [190, 250], 60, "White")
    canvas.draw_text(suc_rate, [400, 60], 50, "Green")
    # draw_text(text, [x, y], 字體大小, 顏色, 字型) 

    
# create frame and timer
f = simplegui.create_frame("Stopwatch", 500, 500)
timer = simplegui.create_timer(100, timer_handler)

# register event handlers
f.add_button("Start", Start, 200)
f.add_button("Stop", Stop, 200)
f.add_button("Reset", Reset, 200)
f.set_draw_handler(draw)

# start frame
f.start()

# Please remember to review the grading rubric
