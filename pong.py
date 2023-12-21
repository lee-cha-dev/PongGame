from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreBoard import ScoreBoard
from divider import Divider
import time

s = Screen()
s.screensize(canvheight=600, canvwidth=800)
s.bgcolor("black")
s.title("Pong")
s.tracer(0)

playerOne = Paddle()
playerTwo = Paddle()

pongBall = Ball(0, 0)

dottedDivider = Divider()

scoreB = ScoreBoard()


def initiatePlayers():
    playerOne.setPlayerPos(400, 0)
    playerTwo.setPlayerPos(-400, 0)


def userQuit():
    playerOne.userQuit()


def quitCheck():
    if playerOne.gameOver:
        return False
    elif not playerOne.gameOver:
        return True


def pOneMovement():
    s.listen()
    s.onkeypress(playerOne.goUp, "Up")
    s.onkeypress(playerOne.goDown, "Down")
    s.onkey(userQuit, "p")


def pTwoMovement():
    s.listen()
    s.onkeypress(playerTwo.goUp, "w")
    s.onkeypress(playerTwo.goDown, "s")


# create a function that creates a multi-thread that handles movement for the
# two players separately. (threads separate from the main one).


def ballBoundaries():  # ceiling/floor
    if pongBall.ycor() > 390 or pongBall.ycor() < -390:
        pongBall.yDirection *= -1
        pongBall.colorChange()


def ballBounce():  # bounced off paddle
    pongBall.xDirection *= -1
    pongBall.bounce()


def detectBall():  # scored
    if pongBall.xcor() > 490:
        pongBall.resetPos()
        pongBall.xDirection *= -1
        scoreB.playerTwoScored()
    if pongBall.xcor() < -520:
        pongBall.resetPos()
        pongBall.xDirection *= -1
        scoreB.playerOneScored()


def ballPlayerCollision():
    if pongBall.distance(playerOne) < 50 and pongBall.xcor() > 370:
        ballBounce()
        pongBall.colorChange()
    elif pongBall.distance(playerTwo) < 50 and pongBall.xcor() < -370:
        ballBounce()
        pongBall.colorChange()


# three threads: one for each of the players, and one for the screen updates.
def Pong():
    pOneMovement()  # add multi-threading to allow both to be used
    pTwoMovement()  # at the same time.
    initiatePlayers()
    gameIsOn = True

    while gameIsOn:
        s.update()
        gameIsOn = quitCheck()
        pongBall.move()
        detectBall()
        ballBoundaries()
        ballPlayerCollision()
        scoreB.scoreBoardVisualCheck()
        time.sleep(pongBall.pongSpeed)


Pong()

s.exitonclick()
