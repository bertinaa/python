from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self): #initializing squares
        self.all_turtles = []
        self.create_snake()
        self.head = self.all_turtles[0]


    def create_snake(self):
        for i in range(3): #this creates the snake body with like 3 squares next to each other
            new_turtle = Turtle("square")
            new_turtle.color("white")
            new_turtle.pu()
            new_turtle.goto(STARTING_POSITIONS[i])
            self.all_turtles.append(new_turtle)

    def move(self):
        for i in range(len(self.all_turtles)-1,0,-1):
            #this loop makes sure that the snake's body is intact and each square doesn't go randomly
            # and also moves the snakes body indefinitely
            self.new_x = self.all_turtles[i-1].xcor()
            self.new_y = self.all_turtles[i - 1].ycor()
            self.all_turtles[i].goto(self.new_x,self.new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            #this condition is so that if a snake is already going up,
            # then it cannot go down in the same path by eating its body
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

