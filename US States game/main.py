import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US STATES GAME")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_screen_coordinates(x,y):
#     print(x,y)
# turtle.onscreenclick(get_screen_coordinates)
# turtle.mainloop()

data = pd.read_csv("50_states.csv")
states = data['state'].to_list()
x = data['x']
y = data['y']

guessed_states = []
while len(guessed_states) < 50:
    user_input = screen.textinput(title=f"{len(guessed_states)}/50 Guessed States",prompt="What is the another state name ?  ").title()
    if user_input=="Exit":
        break
    if user_input in states:
        guessed_states.append(user_input)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        current = data[data.state == user_input]
        t.goto(current.x.item(),current.y.item())
        t.write(user_input)
missing_states = []
for state in states:
    if state not in guessed_states:
        missing_states.append(state)
states_to_learn = pd.DataFrame(missing_states)
states_to_learn.to_csv("States_to_learn.csv")


