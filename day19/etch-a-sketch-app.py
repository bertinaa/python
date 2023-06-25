from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()
screen.listen() #event listener
def move_forwards():
    tim.forward(10)
def move_right():
    tim.right(10)

def move_backwards():
    tim.backward(10)
def move_left():
    tim.left(10)

def clear():
    tim.clear()#clears everything tim has made so far
    tim.pu()
    tim.home() #will bring tim back to the origin
    tim.pd() #pu and pd so we don't trace the entire path back to home/origin
#positional arguments
screen.onkey(move_forwards,"w")
screen.onkey(move_left,"a")
screen.onkey(move_backwards,"s")
screen.onkey(move_right,"d")
screen.onkey(clear,"c")

"""
same thing as keyword arguments
screen.onkey(key="w",fun = move_forwards)
screen.onkey(key="a",fun = move_left)
screen.onkey(key="s",fun = move_backwards)
screen.onkey(key="d",fun = move_right)
"""
screen.exitonclick()
