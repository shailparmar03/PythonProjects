import random
import turtle
from turtle import Turtle,Screen

colours=["red","orange","yellow","green","blue","purple"]
turtles=[]

is_race_on=False
x=-230
y=-100

screen=Screen()
screen.setup(width=500,height= 400)

for color in colours:
    new_turtle = Turtle("turtle")
    new_turtle.color(color)
    turtles.append(new_turtle)
    new_turtle.penup()
    new_turtle.goto(x, y)
    y += 33

user_guess = screen.textinput(title="Make your bet", prompt="Which turtle would win the race?\nEnter colour: ")
if user_guess:
    is_race_on=True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor()>230:
            winner = turtle.pencolor()
            is_race_on=False
            break
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
if user_guess == winner:
    print(f"Yov've won. The {winner} turtle is the winner!")
else:
    print(f"Yov've Lost. The {winner} turtle is the winner!")

screen.exitonclick()