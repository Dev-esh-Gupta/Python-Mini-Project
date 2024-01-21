# import colorgram
#
# colors = colorgram.extract('hirst-paint.jpg',15)
# print(colors)
# rgb_color = []
#
# for color in colors:
#     # rgb_color.append(color.rgb)
#     # print(color)
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_color.append(new_color)
#
# print(rgb_color)
import random
import turtle
from turtle import Turtle, Screen
import random

color_list = [ (198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12)]
turtle.colormode(255)
tim = Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

# for i in range(10):
#     tim.penup()
#     tim.goto(0, 0 + i*30)
#     for _ in range(10):
#         tim.dot(20, random.choice(color_list))
#         tim.forward(50)
#         '''
#         tim.color(random.choice(color_list))
#         tim.pendown()
#         tim.pensize(15)
#         tim.forward(0)
#         tim.penup()
#         tim.forward(30)
#         '''



screen = Screen()
screen.exitonclick()