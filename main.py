import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.generate_car()
    car_manager.move_cars()
    if player.ycor() > 280:
        player.reset_position()
        scoreboard.level_up()
        car_manager.increase_speed()
    if car_manager.check_crash(player):
        scoreboard.game_over()
        game_is_on = False


screen.exitonclick()

