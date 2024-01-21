# import turtle

# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("black", "red")
# timmy.fd(100)
# timmy.left(120)
# timmy.forward(100)
# timmy.home()
# timmy.circle(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()
# table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
# table.add_column("Type",["Electric","Water","Fire"])
table.field_names = ["Pokemon Name", "Type"]
table.add_row(["Pikachu","Electric"])
table.add_row(["Squirtle","Water"])
table.add_row(["Charmander","Fire"])
print(table.align)
# table.border = True
table.padding_width = 5
table.align = "l"

print(table)


