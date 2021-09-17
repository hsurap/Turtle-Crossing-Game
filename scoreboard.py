from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-250,250)
        self.score=1
        self.point(self.score)

    def point(self,score):
        self.clear()
        self.write(f"Level: {score} ",align="Left",font=FONT)

    def game_end(self):
        self.goto(0,0)
        self.write(f"Game Over", align="Center", font=FONT)
