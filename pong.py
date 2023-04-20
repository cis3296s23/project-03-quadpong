# ___QUAD PONG___
# Domenic Malinsky, Rishi Duggal, Tyler Grenell 2023


from turtle import Screen, Turtle
import os
import time
from gameObjs import paddle, ball


class gameRunner:
    def __init__(self, gamemode, points_to_win, ball_count, ball_speed):

        self.gamemode = gamemode
        self.wincon = points_to_win

        self.win = Screen()
        self.win.title("Quad Pong")
        self.win.bgcolor("dark grey")
        self.win.setup(width=1000, height=800)
        self.win.tracer(0)

        self.bd = Turtle()
        self.bd.penup()
        self.bd.goto(-370, -270)
        self.bd.pendown()
        self.bd.pensize(5)
        self.bd.fd(740)
        self.bd.left(90)
        self.bd.fd(540)
        self.bd.left(90)
        self.bd.fd(740)
        self.bd.left(90)
        self.bd.fd(540)
        self.bd.hideturtle()

        if (gamemode == "twoplayer"):
            # TODO make these functions
            twoPlayerInit()
        elif (gamemode == "fourplayer"):
            fourPlayerInit()

        self.pen = Turtle()
        self.pen.speed(0)
        self.pen.shape("square")
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 350)

        self.balls = ball[ball_count]

        for x in self.balls:
            x = ball(ball_speed)

        runGame()
    
    
    
    def twoPlayerInit(self):
        # TODO make this function
        
        self.score1 = 0
        self.score2 = 0

        self.pen.write("Team 1: 0  Team 2: 0", align="center", font=("Courier", 19, "bold"))

        #Paddle A
        self.paddle_a = paddle("red", "v", -340, 0)

        #Paddle B
        self.paddle_b = paddle("blue", "v", 340, 0)

        self.win.listen()
        self.win.onkeypress(self.paddle_a.paddle_up, "w")
        self.win.onkeypress(self.paddle_a.paddle_down, "s")
        self.win.onkeypress(self.paddle_b.paddle_up, "Up")
        self.win.onkeypress(self.paddle_b.paddle_down, "Down")


    def fourPlayerInit(self):
        # TODO make this function
        self.win.listen()
        self.score1 = 0
        self.score2 = 0
        self.pen.write("Team 1: 0  Team 2: 0", align="center", font=("Courier", 19, "bold"))

        #Paddle A
        self.paddle_a = paddle("red", "v", -340, 0)

        #Paddle B
        self.paddle_b = paddle("blue", "v", 340, 0)

        #Paddle C
        self.paddle_c = paddle("green", "h", 0, 250)

        #Paddle D
        self.paddle_d = paddle("purple", "h", 0, -250)
        
        self.win.listen()

        self.win.onkeypress(self.paddle_a.paddle_up, "w")
        self.win.onkeypress(self.paddle_a.paddle_down, "s")
        self.win.onkeypress(self.paddle_b.paddle_up, "Up")
        self.win.onkeypress(self.paddle_b.paddle_down, "Down")

        self.win.onkeypress(self.paddle_c.paddle_left, "a")
        self.win.onkeypress(self.paddle_c.paddle_right, "d")
        self.win.onkeypress(self.paddle_d.paddle_left, "Left")
        self.win.onkeypress(self.paddle_d.paddle_right, "Right")

    def checkIfScore(self, ball):
        if (self.gamemode == "twoplayer"):
            if ball.getx() > 370:
                self.score_1 += 1
                self.pen.clear()
                self.pen.write("Team 1: {}  Team 2: {} ".format(self.score_1, self.score_2), align="center",
                               font=("Courier", 19, "bold"))
                ball.reset()
                ball.dx *= -1

            elif ball.getx() < -370:
                self.score_2 += 1
                self.pen.clear()
                self.pen.write("Team 1: {}  Team 2: {} ".format(self.score_1, self.score_2), align="center",
                               font=("Courier", 19, "bold"))
                ball.reset()
                ball.dx *= -1

        elif (self.gamemode == "fourplayer"):
            if ball.getx() > 370:
                self.score_1 += 1
                self.pen.clear()
                self.pen.write("Team 1: {}  Team 2: {} ".format(self.score_1, self.score_2), align="center",
                               font=("Courier", 19, "bold"))
                ball.reset()
                ball.dx *= -1

            elif ball.getx() < -370:
                self.score_2 += 1
                self.pen.clear()
                self.pen.write("Team 1: {}  Team 2: {} ".format(self.score_1, self.score_2), align="center",
                               font=("Courier", 19, "bold"))
                ball.reset()
                ball.dx *= -1

            elif ball.gety() > 260:
                self.score_1 += 1
                self.pen.clear()
                self.pen.write("Team 1: {}  Team 2: {} ".format(self.score_1, self.score_2), align="center",
                               font=("Courier", 19, "bold"))
                ball.reset()
                ball.dy *= -1

            elif ball.gety() < -260:
                self.score_2 += 1
                self.pen.clear()
                self.pen.write("Team 1: {}  Team 2: {} ".format(self.score_1, self.score_2), align="center",
                               font=("Courier", 19, "bold"))
                ball.reset()
                ball.dy *= -1

    def checkCollisions(self, ball):

        if (self.gamemode == "twoplayer"):

            # RED PADDLE
            if ball.getx() < -317 and ball.gety() < self.paddle_a.gety() + 50 and ball.gety() > self.paddle_a.gety() - 50:
                # prevent side clipping
                ball.setx(-317)
                ball.dx *= -1

                # BLUE PADDLE
            elif ball.getx() > 317 and ball.gety() < self.paddle_b.gety() + 50 and ball.gety() > self.paddle_b.gety() - 50:
                # prevent side clipping
                ball.setx(317)
                ball.dx *= -1

        elif (self.gamemode == "fourplayer"):

            # RED PADDLE
            if ball.getx() < -317 and ball.gety() < self.paddle_a.gety() + 50 and ball.gety() > self.paddle_a.gety() - 50:
                # prevent side clipping
                ball.setx(-317)
                ball.dx *= -1

            # BLUE PADDLE
            elif ball.getx() > 317 and ball.gety() < self.paddle_b.gety() + 50 and ball.gety() > self.paddle_b.gety() - 50:
                # prevent side clipping
                ball.setx(317)
                ball.dx *= -1

            # GREEN PADDLE
            elif ball.gety() > 230 and ball.getx() < self.paddle_c.getx() + 60 and ball.getx() > self.paddle_c.getx() - 60:
                # prevent side clipping
                ball.sety(230)
                ball.dy *= -1

            # PURPLE PADDLE
            elif ball.gety() < -230 and ball.getx() < self.paddle_d.getx() + 60 and ball.getx() > self.paddle_d.getx() - 60:
                # prevent side clipping
                ball.sety(-230)
                ball.dy *= -1

    def runGame(self):
        # TODO make the internal function

        while True:

            self.win.update

            for x in self.balls:
                x.move()

                # Scoring
                checkIfScore(self, x)

                #Collisions
                checkCollisions(self, x)

            
            time.sleep(1/100)



        # TODO handle scoring and collision based on gamemode flag. If statements, or new methods, preferable.