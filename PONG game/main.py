from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from score_board import ScoreBoard




screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("PONG")

screen.tracer(0)
paddle1 = Paddle(350,0)
paddle2 = Paddle(-350,0)
ball = Ball()
score_board = ScoreBoard()


screen.listen()
screen.onkeypress(key="Up",fun=paddle1.move_up)
screen.onkeypress(key="Down",fun=paddle1.move_down)
screen.onkeypress(key="w",fun=paddle2.move_up)
screen.onkeypress(key="s",fun=paddle2.move_down)



game_on = True

while game_on:
    time.sleep(ball.ball_speed)
    ball.move()
    if ball.ycor()>285 or ball.ycor()<-285:
        ball.bounce_y()
    if ball.distance(paddle1) < 50 and ball.xcor()>320 or ball.distance(paddle2) < 50 and ball.xcor()<-320:
        ball.bounce_x()
        ball.ball_speed *= 0.9
    if ball.xcor()>380:
        ball.reset()
        score_board.l_point()

    if ball.xcor()<-380:
        ball.reset()
        score_board.r_point()

    screen.update()



screen.exitonclick()

