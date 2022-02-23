from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self. penup()
        self.hideturtle()
        self.goto(-100, 240)
        self.write(f"Level = {self.level}", align="right", font=FONT)

    def level_up(self):
        self.level +=1
        self.clear()
        self.write(f"Level = {self.level}", align="right", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
