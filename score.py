from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.Remaining = 36
        self.penup()
        self.hideturtle()
        self.clear()
        self.color("sienna")

    def score(self):
        self.goto(0, 350)
        self.write(f"REMAINING = {self.Remaining}", align="center", font=("Arial", 12 , "bold"))

    def update_score(self):
        self.clear()
        self.Remaining = self.Remaining - 1
        self.score()