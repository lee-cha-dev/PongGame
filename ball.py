from turtle import Turtle


class Ball(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.colorArray = ["purple", "blue", "orange"]
        self.shape("circle")
        self.color(self.colorArray[2])
        self.penup()
        self.setposition(x, y)
        self.xDirection = 1
        self.yDirection = 1
        self.colorHold = 0
        self.yMovement = 10
        self.xMovement = 10
        self.pongSpeed = 0.1

    def move(self):
        newX = self.xcor() + (self.xMovement * self.xDirection)
        newY = self.ycor() + (self.yMovement * self.yDirection)
        self.goto(newX, newY)
        self.xMovement = 10

    def colorChange(self):
        if self.colorHold < 3:
            self.color(self.colorArray[self.colorHold])
            self.colorHold += 1
        else:
            self.colorHold = 0
            self.colorChange()

    def resetPos(self):
        self.goto(0, 0)
        self.pongSpeed = 0.1

    def bounce(self):
        self.pongSpeed *= 0.9
