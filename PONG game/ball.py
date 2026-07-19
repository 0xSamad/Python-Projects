from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_amount =10
        self.y_amount = 10
        self.ball_speed = 0.1
    def move(self):
        x_cor = self.xcor() + self.x_amount
        y_cor = self.ycor()+ self.y_amount

        self.goto(x_cor,y_cor)

    def bounce_y(self):
        self.y_amount*= -1

    def bounce_x(self):
        self.x_amount*= -1
        self.ball_speed*=0.9

    def reset(self):
        self.ball_speed = 0.1
        self.goto(0,0)
        self.bounce_x()