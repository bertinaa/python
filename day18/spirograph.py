import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255) #note we tap into the turtle module not object

timmy = Turtle()
timmy.color("SpringGreen")
timmy.speed('fastest')

def change_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    new_tup = (r,g,b) #we use tuple because we do not want anyone to accidentally change the color code
    return new_tup


flag = True
def draw_spirograph(size_of_gap):
  """
  To ensure that the spirograph completes a full revolution, the total angle of rotation needs to be 360 degrees. 
  The value of 360 is divided by size_of_gap to determine the number of iterations needed to complete a full revolution.
For example, if size_of_gap is set to 10, then 360/10 equals 36, which means the loop will iterate 36 times to complete a full revolution.
  """
    timmy.hideturtle()
    for _ in range(int(360/size_of_gap)): 
        timmy.color(change_color())
        timmy.circle(50)
        timmy.setheading(timmy.heading() + size_of_gap)

draw_spirograph(10)
screen = Screen()
screen.exitonclick()


