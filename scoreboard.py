from turtle import Turtle
ALIGMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.high_score = 0

        with open("highscore.txt") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.penup()
        self.setposition(x=0, y=270)
        self.hideturtle()
        self.color("white")
        self.write(f"Score : {self.score} High Score: {self.high_score}", align=ALIGMENT, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} High Score: {self.high_score}", align=ALIGMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #
    #     self.clear()
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align=ALIGMENT, font=FONT)
