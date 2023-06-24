import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255) #note we tap into the turtle module not object

timmy = Turtle()
timmy.color("SpringGreen")

timmy.pensize(10) #width

def change_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    new_tup = (r,g,b) #we use tuple because we do not want anyone to accidentally change the color code
    return new_tup


angle = [0,90,180,270]
screen = Screen()

for _ in range(100): #random turtle walk
    direction = random.choice(angle)
    new_color = change_color()
    timmy.speed("fastest")
    timmy.color(new_color)
    timmy.forward(20)
    timmy.setheading(direction) #will turn left or right
screen.exitonclick()


