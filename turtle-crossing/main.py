import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

player=Player()
car=CarManager()
score=Scoreboard()


screen.listen()
screen.onkeypress(player.go_up,"Up")
game_is_on = True


def detect_collision(all_cars):
    for car in all_cars:
        if car.distance(player) <= 20:
            print("Collision detected")
            global game_is_on
            game_is_on = False
            score.game_over()


while game_is_on:
    time.sleep(0.1)
    car.create_car()
    car.move_cars()
    screen.update()
    detect_collision(car.all_cars)

    # Detect successful crossing
    if player.is_at_finish_line():
        player.goto_start()
        car.level_up()
        score.increase_level()

screen.exitonclick()


