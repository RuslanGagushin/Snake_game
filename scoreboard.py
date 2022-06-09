from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")

with open("HighScore.txt") as file:
    high_score = file.read()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(high_score)
        self.color("cyan")
        self.penup()
        self.goto(0, 270)
        self.update()
        self.hideturtle()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("HighScore.txt", mode="w") as hs:
                hs.write(str(self.high_score))
        self.score = 0
        self.update()

    def increase(self):
        self.score += 1
        self.update()
