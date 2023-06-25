import random
import turtle
from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()

turtle.colormode(255)

colors = [ (202, 166, 109), (152, 73, 47), (170, 153, 41), (222, 202, 138), (53, 93, 124), (135, 32, 22), (132, 163, 184), (48, 118, 88), (198, 91, 71), (16, 97, 75), (100, 73, 75), (67, 47, 41), (147, 178, 147), (163, 142, 156), (234, 177, 165), (55, 46, 50), (130, 28, 31), (184, 205, 174), (41, 60, 72), (83, 147, 126), (181, 87, 90), (31, 77, 84), (47, 65, 83), (215, 177, 182), (19, 71, 63), (175, 192, 212)]

tim.speed('fastest')
tim.pu() #to remove the path traced by the turtle
tim.hideturtle()
"""
in this we don't want the path, so we can simply use pu() and never use pd()
pu() - penup() both are same
pd() - pendown()
"""
tim.setheading(210)
tim.forward(250)
tim.setheading(0)

for i in range(10):
    for j in range(10):
        tim.forward(50)
        tim.dot(20, random.choice(colors)) # size of dot, color are the parameters
    tim.left(90)
    tim.forward(40)
    tim.left(90)
    tim.forward(500)
    tim.right(180)

screen.exitonclick()
