from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.startPos = (350, 0)
        self.gameOver = False

    def goUp(self):
        if self.ycor() <= 340:
            newY = self.ycor() + 20
            self.goto(self.xcor(), newY)

    def goDown(self):
        if self.ycor() >= -340:
            newY = self.ycor() - 20
            self.goto(self.xcor(), newY)

    # player=(350, 0), enemy=(-350, 0)
    def setPlayerPos(self, x, y):
        self.setposition(x, y)

    def userQuit(self):
        self.gameOver = True
