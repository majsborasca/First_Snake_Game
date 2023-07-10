from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        with open("data.txt", mode="r") as file_r:
            self.high_score = int(file_r.read())
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 275)
        self.hideturtle()
        self.update_write()

    def update_write(self):
        self.clear()
        self.write(arg=f"Score: {self.score} / High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reseting(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_write()

    def update_score(self):
        self.score += 1
        self.update_write()






