from turtle import  Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.setposition(-20, 260)
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align="center", font=("Courier", 20, "normal"))
        self.hideturtle()
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align="center", font=("Courier", 20, "normal"))
    def sco(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align="center", font=("Courier", 20, "normal"))