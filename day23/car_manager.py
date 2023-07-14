from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_X_POS = 300


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()
        self.MOVE_SPEED = STARTING_MOVE_DISTANCE

    def create_car(self):
        #to reduce the number of squares we are using the following if statement
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.speed(self.MOVE_SPEED)
            new_car.pu()
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.color(random.choice(COLORS))
            y_pos = random.randint(-250, 250)
            new_car.goto(STARTING_X_POS, y_pos)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.MOVE_SPEED)


    #increasing the speed of the cars as we level up!
    def move_increment(self):
        self.MOVE_SPEED += MOVE_INCREMENT
