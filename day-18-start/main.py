import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
tim = Turtle()
tim.shape("turtle")
tim.color("DarkOrchid3")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)

#Challenge 1
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

#Challenge 2
# for _ in range(50):
#     tim.forward(3)
#     tim.penup()
#     tim.forward(2)
#     tim.pendown()

#Challenge3
'''
col = ["red","blue","green"]
for i in range(3,11):
    tim.color(col[i%3])
    for _ in range(i):
        tim.forward(100)
        tim.right(360/i)
'''

#Challenge4
'''
col = ["DarkRed","khaki","LightBlue","ForestGreen","brown","gold","DeepSkyBlue2","green","coral","yellow"]
direction = [0,90,180,270]
tim.width(15)
tim.speed(10)
for _ in range(200):
    # tim.color(random.choice(col))
    tim.color(random_color())
    tim.fd(30)
    tim.setheading(random.choice(direction))
'''

#Challenge5
tim.speed("fastest")
def spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+size_of_gap)

spirograph(5)
















screen = Screen()
screen.exitonclick()

