from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.penup()
        self.hideturtle()

        self.lScore = 0
        self.rScore = 0

        self.gameOver = False

        self.goto(-100, 300)
        self.write(self.lScore, align=ALIGNMENT, font=FONT)
        self.goto(100, 300)
        self.write(self.rScore, align=ALIGNMENT, font=FONT)

        # divider
        self.goto(0, 400)
        self.setheading(270)
        while self.ycor() > -400:
            self.color("red")
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)

    def playerOneScored(self):
        self.rScore += 1
        self.clear()
        self.updateScores()

    def playerTwoScored(self):
        self.lScore += 1
        self.clear()
        self.updateScores()

    def updateScores(self):
        self.goto(-100, 300)
        self.write(self.lScore, align=ALIGNMENT, font=FONT)
        self.goto(100, 300)
        self.write(self.rScore, align=ALIGNMENT, font=FONT)

    def scoreBoardVisualCheck(self):
        if self.lScore > self.rScore:
            self.clear()
            self.color("green")
            self.goto(-100, 300)
            self.write(self.lScore, align=ALIGNMENT, font=FONT)
            self.color("red")
            self.goto(100, 300)
            self.write(self.rScore, align=ALIGNMENT, font=FONT)
        elif self.rScore > self.lScore:
            self.clear()
            self.color("green")
            self.goto(100, 300)
            self.write(self.rScore, align=ALIGNMENT, font=FONT)
            self.color("red")
            self.goto(-100, 300)
            self.write(self.lScore, align=ALIGNMENT, font=FONT)
        elif self.rScore == self.lScore:
            self.clear()
            self.color("yellow")
            self.goto(100, 300)
            self.write(self.rScore, align=ALIGNMENT, font=FONT)
            self.color("yellow")
            self.goto(-100, 300)
            self.write(self.lScore, align=ALIGNMENT, font=FONT)
