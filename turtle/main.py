import random
import turtle
from turtle import Turtle,Screen


tim=Turtle()
tim.shape("turtle")
tim.color("red")
# for _ in range(4):
#     timmy_turtle.forward(100)
#     timmy_turtle.right(90)
# for _ in range(50):
#     timmy_turtle.forward(2)
#     timmy_turtle.penup()
#     timmy_turtle.forward(2)
#     timmy_turtle.pendown()

# def draw_shape(n_sides):
#     for _ in range(n_sides):
#         timmy_turtle.forward(50)
#         timmy_turtle.right(360/n_sides)
#
# for n_sides_shape in range(3,11):
#     draw_shape(n_sides_shape)


########### Challenge 4 - Random Walk ########
turtle.colormode(255)

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return(r,g,b)

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions=[0,90,180,270]
# tim.pensize(10)
tim.speed("fastest")
# for _ in range(2000):
#     # tim.color(random.choice(colours))
#     tim.color(random_colour())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

########### Challenge 4 - Circle pattern ########
angle=0
for _ in range(int((360/10)+1)):
    turtle.circle(100)
    turtle.color(random_colour())
    angle += 10
    turtle.setheading(angle)




screen=Screen()
screen.exitonclick()




