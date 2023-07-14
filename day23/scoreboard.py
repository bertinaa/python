FONT = ("Arial", 24, "bold")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.goto(-280,260)
        self.update_score()
        self.hideturtle()
        self.pu()


    def update_score(self):
        self.clear()
        self.write(f"Level : {self.score}",font= FONT,align="left")

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game over.", font=FONT, align="center")


