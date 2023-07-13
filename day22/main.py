from turtle import Screen, Turtle
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.bgcolor("black")
screen.title("Ping Pong.")
screen.setup(width=1000, height=600)

screen.tracer(0)

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_on = True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collisions with wall - making the ball bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    #detect collisions with paddle
    if (ball.xcor() > 320 and ball.distance(r_paddle) < 50) or (ball.xcor() < -320 and ball.distance(l_paddle) < 50):
        # less than 50 and not 20 because distance measures distance from center
        # of the ball to center of the paddle
        #paddle is at (340,0) pos hence ball.xcor() > 330
        ball.paddle_bounce()

    #detect when both paddles miss
    elif ball.xcor() < -380:
        ball.center()
        scoreboard.r_point()

    elif  ball.xcor() > 380:
        ball.center()
        scoreboard.l_point()










screen.exitonclick()
