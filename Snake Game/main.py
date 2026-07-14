from turtle import Screen
from snake import Snake
from food import Food
from score_board import Scoreboard

import random
import time

screen = Screen()
screen.tracer(0)
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
snake = Snake()
food = Food()
score_board = Scoreboard()

screen.listen()

screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Left",fun=snake.left)
screen.onkey(key="Right",fun=snake.right)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.snake_parts[0].distance(food)<15:
        food.refresh()
        snake.extend()
        score_board.increase_score()
    if snake.snake_parts[0].xcor() >=299 or snake.snake_parts[0].xcor() <=-299 or snake.snake_parts[0].ycor() >=299 or snake.snake_parts[0].ycor() <=-299:
        game_on = False
        score_board.game_over()
    for snake_part in snake.snake_parts:
        if snake_part == snake.snake_parts[0]:
            pass
        elif snake.snake_parts[0].distance(snake_part)<10:
            game_on=False
            score_board.game_over()


screen.exitonclick()