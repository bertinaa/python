from turtle import Turtle

MAX_Y = 250
DISTANCE = 20

class Paddle(Turtle):
    def __init__(self,xy):
        super().__init__()
        self.pu()
        self.shape("square")
        self.color("white")
        '''
        all paddles will start with 20 x 20 by default
        we need width = 20, length = 100
        '''
        self.shapesize(stretch_wid=5, stretch_len=1)
        # self.setx(x)
        # self.sety(y)
        self.goto(xy)

    def up(self):
        if self.ycor() < MAX_Y:
            new_y = self.ycor() + DISTANCE
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() > -MAX_Y:
            new_y = self.ycor() - DISTANCE
            self.goto(self.xcor(), new_y)
