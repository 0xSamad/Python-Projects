from tkinter import *
import pandas as pd
import random
to_learn ={}


try:
    data = pd.read_csv("data/to_learn_words.csv")
except:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

card = {}

def is_known():
    to_learn.remove(card)
    next_card()
    new_data = pd.DataFrame(to_learn)
    new_data.to_csv("data/to_learn_words.csv",index=False)
def next_card():
    global card
    global flip_timer
    window.after_cancel(flip_timer)
    card = random.choice(to_learn)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=card['French'],fill="black")
    canvas.itemconfig(card_background,image=card_front)
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=card["English"],fill="white")
    canvas.itemconfig(card_background,image=card_back)


BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)
window.title("Capstone Project")

flip_timer = window.after(3000,flip_card)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")


canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card_background = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400,150,text="Title",font=("Arial",24,"italic"))
card_word = canvas.create_text(400,263,text="Text",font=("Arial",35,"bold"))
canvas.grid(row=0,column=0,columnspan=2)


tick = PhotoImage(file="images/right.png")
cross = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross,highlightthickness=0,command=next_card)
unknown_button.grid(row=1,column=0)
known_button = Button(image=tick, highlightthickness=0,command=is_known)
known_button.grid(row=1,column=1)

next_card()

window.mainloop()



