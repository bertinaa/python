from turtle import Turtle,Screen
import random

is_race_on = True
screen = Screen()
screen.setup(width=600, height=500) #width, height of the screen, keyword argument
#screen.setup(500,400) positional arguments

#pop up for getting the bet from the user, this works similar to input()
user_bet = screen.textinput(title="Place your bet",prompt="Which turtle do you think is going to win? : ")

"""
initialization
shape
pu
color
"""
all_turtles = []

color = ["orange","blue","green","purple","red","black","yellow","pink"]
x = -250
y = 200
for i in range(8):
    new_turtle = Turtle(shape="turtle")
    new_turtle.speed("fastest")
    new_turtle.pu()
    new_turtle.color(color[i])
    y = y-50
    new_turtle.goto(x, y)
    all_turtles.append(new_turtle)

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 270:
            winning_color = turtle.pencolor()
            is_race_on = False
        distance = random.randrange(0, 10)
        turtle.forward(distance)

if user_bet == winning_color:
    print(f"You won! the {winning_color} placed first :)")
else:
    print(f"You lost! the {winning_color} placed first :/")

screen.exitonclick()
