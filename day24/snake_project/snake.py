from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self): #initializing squares
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for pos in STARTING_POSITIONS: #this creates the snake body with like 3 squares next to each other
            self.add_segment(pos)

    def reset(self): #deleting current snake once the snake hits a wall/ bites its body off
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0] #we have to do everything to initialize again and get the game running

        '''
        turtle.clear() //segments.clear()
        Delete the turtle’s drawings from the screen. *Do not move turtle.*
        State and position of the turtle as well as drawings of other turtles are not affected.

        so basically clear will only clear the lines of the turtle and then the turtle will stay at the position
        it was last seen, hence we need to remove it from the screen
        hence the for loop
                for seg in self.segments:
                    seg.goto(1000,1000)

        '''

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            #this loop makes sure that the snake's body is intact and each square doesn't go randomly
            # and also moves the snakes body indefinitely
            self.new_x = self.segments[i - 1].xcor()
            self.new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(self.new_x, self.new_y)
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self,i):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.pu()
        new_segment.goto(i)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())
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


