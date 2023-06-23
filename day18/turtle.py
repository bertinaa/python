from turtle import Turtle, Screen
timmy = Turtle()
timmy.shape("turtle")
timmy.color("SpringGreen")
#triangle, square, pentagon
#hexagon, heptagon, octagon
#nonagon, decagon
"""
360/no_of_sides will give us the degree each shape has
shapes() will draw from triangle till decagon!
"""

def shapes(sides):
    shape = sides
    while shape:
        timmy.forward(100)
        turn_angle = 360 / sides
        timmy.right(turn_angle)
        shape -=1

for side in range(3,11):
    shapes(side)




# for _ in range(4): #draw dashed lines
#     timmy.forward(20)
#     timmy.pu()
#     timmy.forward(20)
#     timmy.pd()

# for _ in range(4): #draw a square
#     timmy.forward(200)
#     timmy.right(90)



screen = Screen()
screen.exitonclick()
