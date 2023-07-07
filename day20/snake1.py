from turtle import Turtle,Screen
screen = Screen()
screen.bgcolor("black")
screen.setup(600,600)
screen.title("Snake Game.")

snake = Turtle(shape="square")
snake.color("white")
snake.pu()
snake.speed("fastest")

#snake.shapesize(stretch_wid= 1,stretch_len=3)

snake1 = Turtle(shape="square")
snake1.color("white")
snake1.pu()
snake1.speed("fastest")
snake1.goto(-20,0)

snake2 = Turtle(shape="square")
snake2.color("white")
snake2.pu()
snake2.speed("fastest")
snake2.goto(-40,0)



screen.exitonclick()
