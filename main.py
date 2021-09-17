import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
scoreboard=Scoreboard()
screen.tracer(0)
player=Player()
screen.listen()
car_manager = CarManager()
screen.onkey(fun=player.move,key="Up")

screen.setup(width=600, height=600)

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()
    car_manager.making_random_cars()
    car_manager.move_cars()

    if player.ycor()>280:
        scoreboard.score+=1
        scoreboard.point(scoreboard.score)
        player.level_up()
        car_manager.increase_speed()

    for i in car_manager.all_cars:
        if player.distance(i)<20:
            scoreboard.game_end()
            game_is_on=False


screen.exitonclick()