from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        #by default the food size will be 20 pixels so we are halving it by doing the 0.5
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        #used to make food appear at random
        random_x = random.randint(-280,280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
