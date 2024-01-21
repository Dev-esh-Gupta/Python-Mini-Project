from turtle import Turtle
ALIGNMENT = "center"
FONT =('courier', 15, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(-20,270)
        self.write(f"Score : {self.score} ", align=ALIGNMENT, font=FONT)
        self.hideturtle()
        # self.scoreUpdate()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def score_update(self):
        self.clear()
        self.score += 1
        self.write(f"Score : {self.score} ", align=ALIGNMENT, font=FONT)
