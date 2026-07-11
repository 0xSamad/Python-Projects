from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500,height=400)

colors = ['red','green','blue','black','brown','yellow']

turtles = []

for i in range(len(colors)):

    turtle_object = Turtle("turtle")
    turtle_object.color(colors[i])
    turtles.append(turtle_object)

size = -50

for tur in turtles:
    tur.penup()
    tur.goto(-238,size)
    size+=25

user_bet = screen.textinput(title="Make A Chocie: ", prompt="Which Turtle will win the race ? Select a color : ")
is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:

    for tur in turtles:
        random_distance = random.randint(0,10)
        tur.forward(random_distance)
        if tur.xcor()> 230:
            is_race_on = False
            winning_color = tur.pencolor()
            if user_bet == winning_color:
                print(f"You won . The {winning_color} turtle is the winner")
            else:
                print(f"you have lost. The {winning_color} turtle is the winner")
                break

screen.exitonclick()