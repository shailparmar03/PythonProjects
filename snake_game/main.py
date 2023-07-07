import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)


snake=Snake()
food =Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# #TODO 1. Create a snake body
# snake.create_snake()

#TODO 2. Move the snake
game_is_on =True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    snake.move()

    if snake.head.distance(food) < 15:
        print("Collided")
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280   :
        # game_is_on=False
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1::]:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            # scoreboard.game_over()
            scoreboard.reset()
            snake.reset()


screen.exitonclick()