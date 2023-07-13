from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def wall_bounce(self):
        self.y_move *= -1
        #cause everytime we hit a wall, y alone changes!

    def paddle_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9
        #every time we hit the paddle, speed increases! but we cannot have a very high speed

    def center(self):
        self.goto(0,0)
        #since we cannot have a very high speed
        self.move_speed = 0.1
        self.x_move *= -1
        self.move()





