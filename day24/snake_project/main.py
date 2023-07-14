MOVE_DISTANCE = 20
from turtle import Screen
from food import Food
import time
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    snake.move()
    screen.update()
    time.sleep(0.1)

    # detecting wall collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # note less than! failure as an engg graduate tch tch tch
        score_board.reset()
        snake.reset()

    # detecting collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increase_score()

    # detecting if snake is biting off its own body
    for segment in snake.segments[1:]:
        # slicing cause we don't want it to check the first segment which is the head cause of the if condition below!
        if snake.head.distance(segment) < 10:
            score_board.reset()
            snake.reset()

screen.exitonclick()
