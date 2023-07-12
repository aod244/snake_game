from turtle import Turtle
ALIGMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.setposition(x=0, y=270)
        self.hideturtle()
        self.color("white")
        self.write(f"Score : {self.score}", align=ALIGMENT, font=FONT)

    def refresh_score(self):

        self.clear()
        self.score += 1
        self.write(f"Score : {self.score}", align=ALIGMENT, font=FONT)

    def game_over(self):

        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGMENT, font=FONT)
