import turtle


screen = turtle.Screen()
screen.title("India States Game")

image = "indiaMap.gif"
screen.addshape(image)
turtle.shape(image)
turtle.setup(700,750)

def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()

screen.exitonclick()