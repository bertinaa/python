from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.color("white")
        self.pu()
        self.goto(0,280)
        self.update_score()

    def update_score(self):
        self.clear() #to avoid overlapping of all the self.write() lines
        #we need to increase score and then show the Score by calling update_score
        self.write(f"Score : {self.score} Highscore : {self.high_score}", align=ALIGNMENT, font=FONT)
    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0 #resetting score to 0 to start from the beginning
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game over.",align=ALIGNMENT,font=FONT)


