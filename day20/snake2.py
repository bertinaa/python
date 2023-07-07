from turtle import Turtle,Screen
screen = Screen()
screen.bgcolor("black")
screen.setup(600,600)
screen.title("Snake Game.")

positions = [(0,0),(-20,0),(-40,0)]

for position in positions:
    snake = Turtle(shape="square")
    snake.speed("fastest")
    snake.color("white")
    snake.pu()
    snake.goto(position)


screen.exitonclick()
