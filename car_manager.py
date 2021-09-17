from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars=[]
        self.move_dist=STARTING_MOVE_DISTANCE
        self.inc=MOVE_INCREMENT
        self.making_random_cars()

    def making_random_cars(self):
        random_chance=random.randint(1,6)
        if random_chance==1:
            new_car=Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            x_cor = 300
            y_cor = random.randint(-250, 250)
            new_car.goto(x_cor, y_cor)
            self.all_cars.append(new_car)

    def move_cars(self):
        for i in self.all_cars:
            i.backward(self.move_dist)

    def increase_speed(self):
        self.move_dist+=self.inc




