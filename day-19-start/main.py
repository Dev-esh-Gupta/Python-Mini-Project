import turtle
from turtle import Turtle, Screen

'''
tim = Turtle()
screen = Screen()

# Project Etch Sketch
def move_forward():
    tim.forward(15)

def move_backward():
    tim.backward(15)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear,"c")

'''

#Turtle Racing Game
import random
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtle = []
print(f"Bet Color : {user_bet}")

for turtle_index in range(0,6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    # tim.shape("turtle")
    new_turtle.goto(x=-230, y=-100 + turtle_index * 40)
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                print(f"You've Won! the Race and Winning color is {winner_color}")
            else:
                print(f"You've loose! the Race and Winning color is {winner_color}")
            is_race_on = False

        rand_dist = random.randint(0,10)
        turtle.forward(rand_dist)

screen.exitonclick()