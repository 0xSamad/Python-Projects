import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
cars = CarManager()
screen.setup(width=600, height=600)
screen.tracer(0)

score_board = Scoreboard()
player = Player()
screen.listen()
screen.onkeypress(key="Up",fun=player.go_up)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_cars()

    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score_board.game_over()
    if player.is_at_finish():
        player.go_to_start()
        cars.level_up()
        score_board.increase_level()
screen.exitonclick()
