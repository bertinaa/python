from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.pu()
        self.goto(0,280)
        self.update_score()

    def update_score(self):
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)
    def increase_score(self):
        self.score += 1
        self.clear() #to avoid overlapping of all the self.write() lines
        #we need to increase score and then show the Score by calling update_score
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game over.",align=ALIGNMENT,font=FONT)


