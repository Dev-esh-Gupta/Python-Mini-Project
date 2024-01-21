from turtle import Screen
from paddle import Paddle
from ball import Ball
import scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# paddle = Turtle("square")
# paddle.color("white")
# paddle.shapesize(stretch_wid=5,stretch_len=1)
# paddle.penup()
# paddle.goto(350,0)
#
#
# def up():
#     new_y = paddle.ycor() + 20;
#     paddle.goto(paddle.xcor(),new_y)
#
#
# def down():
#     new_y = paddle.ycor() - 20;
#     paddle.goto(paddle.xcor(),new_y)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = scoreboard.Scoreboard()


screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #needs to bounce
        ball.bounce_y()


    #Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320\
            or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect Right missing of paddle
    if ball.xcor() > 380 :
        ball.reset_position()
        scoreboard.l_point()

    # Detect Left missing of paddle
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()