import time
from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen=Screen()
score=Scoreboard()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

ball=Ball()
r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        # Ball needs to bounce
        ball.bounce_y()

    # To detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() >= 330 or ball.distance(l_paddle) < 50 and ball.xcor() <= -330:
        print("Made contact")
        ball.bounce_x()

    # Detect when the right paddle misses
    if ball.xcor() >=380:
        ball.reset_position()
        score.l_point()

    # Detect when the right paddle misses
    if ball.xcor() <= -380:
        ball.reset_position()
        score.r_point()






screen.exitonclick()
