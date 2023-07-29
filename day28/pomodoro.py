from tkinter import *
import math
import winsound

"""
Pomodoro
1st rep 25 min work
2nd rep 5 min break
3rd rep 25 min work
4th rep 5 min break
5th rep 25 min work
6th rep 5 min break
7th rep 25 min work
8th rep 20 min break

"""

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():

    window.after_cancel(timer) #stop everything that window.after() did
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():

    work_sec = WORK_MIN * 60
    break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    global reps
    reps += 1

    if reps%8==0:
        countdown(long_break_sec)
        title.config(text="Break", fg=RED)
    elif reps%2==0:
        countdown(break_sec)
        title.config(text="Break", fg=PINK)
    else:
        countdown(work_sec)
        title.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global timer
    count_min = math.floor(count/60)
    count_sec = count%60

    canvas.itemconfig(timer_text,text=f"{count_min:02}:{count_sec:02}") # format 05:00
    # you cannot do canvas.config here while working with Canvas
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
        # after 1000ms = 1s, call the count down function and then decrease count by 1
    else:
        winsound.Beep(1000, 1000)
        start_timer()

    mark = ""
    work_sessions = math.floor(reps/2)
    for _ in range(work_sessions):
        mark+="✔"
    check_marks.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

# canvas allows you to have overlapping
# in this case, we are going to be having some text over an image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# PhotoImage will tap into the picture
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
# fill is the color of the text
canvas.grid(row=1, column=1)


title = Label()
title.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
title.grid(row=0, column=1)

start = Button(text="Start", highlightthickness=0, bg="white",borderwidth=0,command=start_timer)
start.grid(row=2, column=0)

reset = Button(text="Reset", highlightthickness=0, bg="white",borderwidth=0,command=reset_timer)
reset.grid(row=2, column=2)

check_marks = Label()
check_marks.config(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"))
check_marks.grid(row=3, column=1)

window.mainloop()
