from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,x_cor,y_cor):
        super().__init__()
        self.shape("square")
        self.penup()
        self.goto(x_cor, y_cor)
        self.color("white")
        self.turtlesize(stretch_wid=5, stretch_len=1)

    def move_up(self):
        new_y = self.ycor() + 20
        if new_y < 280:  # keep paddle from going off the top
            self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        if new_y > -280:  # keep paddle from going off the bottom
            self.goto(self.xcor(), new_y)

