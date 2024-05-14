from tkinter import *
import math
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
timer = NONE
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(timer)  # Stops the current pomodoro session so it can start over
    # timer_text 00:00
    canvas.itemconfig(timer_text, text="00:00")
    # title_label "Timer"
    title_label.config(text="Timer")
    # reset check_marks
    check_marks.config(text="")  # Starts out without any checkmarks
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    # If it's 8th rep:
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Long Break", fg=RED)
    # If it's the 2nd, 4th, 6th rep:
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Short Break", fg=PINK)
    # If it's the 1st, 3rd, 5th, 7th rep:
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):

    count_min = math.floor(count / 60)  # Defines the amount of minutes left
    count_sec = count % 60  # Defines the amount of seconds left
    # if count_sec == 0:
    #     count_sec = "00"
    if count_sec < 10:
        count_sec = f"0{count_sec}"  # Makes it so the numbers are formatted whenever there's less than 10 seconds left

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer  # Brings out the global variable timer to be used in the count_down function
        timer = window.after(1000, count_down, count - 1)  # This will make the count go down by 1 every second
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"  # Adds a checkmark after every work+break session
        check_marks.config(text=marks, fg=GREEN, bg=YELLOW)  # Defines the checkmark's attributes


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()  # Creates the window with tkinter
window.title("Pomodoro")  # Names the window
window.config(padx=100, pady=50, bg=YELLOW)  # Defines the window's attributes


# def say_something(a, b, c):
#     print(a)
#     print(b)
#     print(c)


# window.after(1000, say_something, 3, 5, 8)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))  # Creates a title text
# if reps % 8 == 0:
#     timer = Label(text="Long Break", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
# elif reps % 2 == 0:
#     timer = Label(text="Short Break", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
# elif reps % 2 != 0:
#     timer = Label(text="Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
title_label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)  # Creates a start button at the top
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)  # Creates a reset button at the bottom
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

# fg=GREEN
# text="✔"
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # Defines the canvas' attributes
tomato_img = PhotoImage(file="tomato.png")  # Creates a variable for the tomato image
canvas.create_image(100, 112, image=tomato_img)  # Uses the tomato image to fill out the canvas
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))  # Adds a timer text
# canvas.pack()
canvas.grid(column=1, row=1)  # Positions the canvas at the center of the screen
# count_down(5 * 60)

window.mainloop()
