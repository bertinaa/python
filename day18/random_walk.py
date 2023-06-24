from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.color("SpringGreen")

timmy.pensize(10) #width

colors = ["CornflowerBlue", "MediumTurquoise", "MediumSlateBlue", "Orchid", "PaleVioletRed", "Firebrick",
              "Gold", "LightSlateGray"]

angle = [0,90,180,270]
screen = Screen()

for _ in range(100): #random turtle walk
    direction = random.choice(angle)
    new_color = random.choice(colors)
    timmy.speed("fastest")
    timmy.color(new_color)
    timmy.forward(20)
    timmy.setheading(direction) #will turn left or right
screen.exitonclick()


