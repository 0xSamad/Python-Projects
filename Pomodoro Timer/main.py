from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 5
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps =0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(count_down_text,text="00:00")
    timer_label.config(text="Timer")
    check.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps%8==0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=PINK)
    elif reps%2==0:
        timer_label.config(text="Break",fg=PINK)
        count_down(short_break_sec)
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(count_down_text,text=f"{count_min}:{count_sec}")
    if count> 0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        checks = ""

        for _ in range(math.floor(reps/2)):
            checks += "✔️"
        check.config(text=checks)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas = Canvas(width=220,height=223,bg=YELLOW,highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(110,112, image=photo)
count_down_text = canvas.create_text(103,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)

timer_label = Label(text="Timer",bg=YELLOW,fg=GREEN,font=(FONT_NAME,35,"bold"))
timer_label.grid(row=0,column=1)

start = Button(text="START",bg=YELLOW,fg="black",font=(FONT_NAME,14,"bold"),highlightthickness=0,command=start_timer)
start.grid(row=2,column=0)
stop = Button(text="RESET",bg=YELLOW,fg="black",font=(FONT_NAME,14,"bold"),highlightthickness=0,command=reset_timer)
stop.grid(row=2,column=2)

check = Label(text="",fg=GREEN,bg=YELLOW,font=("Arial",20,"bold"))
check.grid(row=3,column=1)

window.mainloop()