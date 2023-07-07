import random

import colorgram
import  turtle
# rgb_colors=[]
# colors=colorgram.extract('C:\\Users\\158311\\Desktop\\BVM\\udemyChallenges\\turtle\\hirstPainting\\download.jpg',10)
# for color in colors:
#     rgb_colors.append((color.rgb.r,color.rgb.g,color.rgb.b))
#
# print(rgb_colors)
turtle.colormode(255)
color_list = [(197, 165, 117), (142, 80, 56), (220, 201, 137), (59, 94, 119), (164, 152, 53), (136, 162, 181)]

tim = turtle.Turtle()
tim.setheading(230)
tim.penup()
tim.hideturtle()
tim.forward(250)
tim.setheading(0)

for __ in range(10):
    for _ in range(10):
        tim.pendown()
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)
    tim.setheading(90)
    tim.forward(30)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)


screen=turtle.Screen()
screen.exitonclick()