import tkinter

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK="🗸"
MARKS=""
REPS = 0
timer= None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global MARKS,REPS
    window.after_cancel(timer)
    title_label.config(text="Timer",fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    MARKS=""
    REPS=0
    check_marks.config(text=MARKS)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS,MARKS
    REPS+=1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec= LONG_BREAK_MIN * 60

    # count_down(5*60)
    if REPS == 8:
        title_label.config(text="Break", fg=RED)
        count_down(long_break_sec)

    elif REPS%2 == 0:
        MARKS+=CHECKMARK
        check_marks.config(text=MARKS)
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)

    else:
        title_label.config(text="Work")
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = int(count/60)
    count_sec = count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer = window.after(1000,count_down, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

tomato_img = tkinter.PhotoImage(file="tomato.png")

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112,image=tomato_img)
timer_text = canvas.create_text(100, 130,text="00:00", fill="white", font=(FONT_NAME,32,"bold"))

canvas.grid(row=1,column=1)

# timer label
title_label=tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW,font=(FONT_NAME,32,"bold"))
title_label.grid(row=0,column=1)

# buttons
start_button = tkinter.Button(text="Start", highlightthickness=0,command = start_timer)
start_button.grid(row=2, column=0)
reset_button = tkinter.Button(text="Reset", highlightthickness=0,command=reset_timer)
reset_button.grid(row=2, column=2)

# Checkmark Label
check_marks=tkinter.Label(fg=GREEN,bg=YELLOW,font=("bold"))
check_marks.grid(row=4,column=1)

window.mainloop()
