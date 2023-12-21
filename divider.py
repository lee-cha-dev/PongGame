from turtle import Turtle


class Divider(Turtle):
    def __init__(self):
        super().__init__()
        self.color("silver")
        self.hideturtle()
        self.penup()
        self.width(3)
        self.goto(0, 400)
        self.setheading(270)
        while self.ycor() > -400:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
