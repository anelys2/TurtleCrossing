from turtle import Turtle
FONT = ("Courier", 12, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-270, 260)
        self.level = 1
        self.write(f"Level: {self.level}", align="left", font=FONT)
        self.color("black")

    def update_score(self):
        self.clear()
        self.level += 1
        self.goto(-270, 260)
        self.write(f"Level: {self.level}", align="left", font=FONT)
        self.color("black")

    def game_over(self):
        self.goto(0,0)
        self.color("black")
        self.write("Game over!", align="center", font=FONT)

