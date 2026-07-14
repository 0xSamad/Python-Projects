from turtle import Turtle,Screen
import random
import time


UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180
positions = [(0,0),(-20,0),(-40,0)]

class Snake:
    def __init__(self):
        self.snake_parts = []
        for position in positions:
            self.add_segment(position)



    def add_segment(self,position):
        square = Turtle('square')
        square.color('white')
        square.penup()
        square.goto(position)
        self.snake_parts.append(square)
    def extend(self):
        self.add_segment(self.snake_parts[-1].position())


    def move(self):
        for i in range(len(self.snake_parts) - 1, 0, -1):
            x_cor = self.snake_parts[i - 1].xcor()
            y_cor = self.snake_parts[i - 1].ycor()
            self.snake_parts[i].goto(x_cor, y_cor)
        self.snake_parts[0].forward(20)


    def up(self):
        if self.snake_parts[0].heading()!=DOWN:
            self.snake_parts[0].setheading(UP)
    def down(self):
        if self.snake_parts[0].heading() != UP:
            self.snake_parts[0].setheading(DOWN)
    def right(self):
        if self.snake_parts[0].heading() != LEFT:
            self.snake_parts[0].setheading(RIGHT)
    def left(self):
        if self.snake_parts[0].heading() != RIGHT:
            self.snake_parts[0].setheading(LEFT)
