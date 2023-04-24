# ___QUAD PONG___
# Domenic Malinsky, Rishi Duggal, Tyler Grenell 2023


from turtle import Screen, Turtle, TurtleScreen 
import os
import time
from gameObjs import paddle, ball
import splashscreen 

class gameRunner:
    def __init__(self, gamemode, points_to_win, ball_count, ball_speed):

        self.gamemode = gamemode
        self.wincon = points_to_win
        self.exit_flag = 0

        TurtleScreen._RUNNING = True

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

        if(gamemode == "twoplayer" or gamemode == "2pRally"):
            self.twoPlayerInit()
        elif(gamemode == "fourplayer" or gamemode == "4pRally"):
            self.fourPlayerInit()    
        
        self.balls = []

        for x in range(ball_count):
            self.balls.append(ball(ball_speed))
           

        self.pen = Turtle()
        self.pen.speed(0)
        self.pen.shape("square")
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 350)

        if (gamemode == "2pRally" or gamemode == "4pRally"):
            self.pen.write("Consecutive Hits: 0 ", align="center",
                           font=("Courier", 19, "bold"))
        elif (gamemode == "twoplayer" or "fourplayer"):
            self.pen.write("Team 1: 0  Team 2: 0", align="center", font=("Courier", 19, "bold"))

        self.exit_button = Turtle()
        self.exit_button.shape("square")
        self.exit_button.color("white")
        self.exit_button.shapesize(stretch_wid=2,stretch_len=3)
        self.exit_button.penup()
        self.exit_button.hideturtle()
        self.exit_button.goto(0, -375)
        self.exit_button.onclick(self.exitGame)
        self.exit_button.showturtle()

        self.exit_header = Turtle()
        self.exit_header.shape("square")
        self.exit_header.color("white")
        self.exit_header.penup()
        self.exit_header.hideturtle()
        self.exit_header.goto(0, -360)
        self.exit_header.write("Exit to Main Menu", align="center", font=("Courier", 19, "bold"))


        self.runGame()
    
    
    
    def twoPlayerInit(self):
        # TODO make this function
        
        self.score1 = 0
        self.score2 = 0

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
        self.score1 = 0
        self.score2 = 0

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
            if ball.getx() > 360:
                self.score1 += 1
                self.pen.clear()
                self.pen.write("Team 1: {}  Team 2: {} ".format(self.score1, self.score2), align="center",
                               font=("Courier", 19, "bold"))
                ball.reset()
                ball.dx *= -1

            elif ball.getx() < -360:
                self.score2 += 1
                self.pen.clear()
                self.pen.write("Team 1: {}  Team 2: {} ".format(self.score1, self.score2), align="center",
                               font=("Courier", 19, "bold"))
                ball.reset()
                ball.dx *= -1

        elif (self.gamemode == "2pRally"):
            if ball.getx() > 360:
                self.score1 = 0
                self.pen.clear()
                self.pen.write("Consecutive Hits: {} ".format(self.score1), align="center",
                               font=("Courier", 19, "bold"))
                ball.reset()
                ball.dx *= -1

            elif ball.getx() < -360:
                self.score1 = 0
                self.pen.clear()
                self.pen.write("Consecutive Hits: {} ".format(self.score1), align="center",
                               font=("Courier", 19, "bold"))
                ball.reset()
                ball.dx *= -1

        elif (self.gamemode == "fourplayer"):
            if ball.getx() > 360:
                self.score1 += 1
                self.pen.clear()
                self.pen.write("Team 1: {}  Team 2: {} ".format(self.score1, self.score2), align="center",
                               font=("Courier", 19, "bold"))
                ball.reset()
                ball.dx *= -1

            elif ball.getx() < -360:
                self.score2 += 1
                self.pen.clear()
                self.pen.write("Team 1: {}  Team 2: {} ".format(self.score1, self.score2), align="center",
                               font=("Courier", 19, "bold"))
                ball.reset()
                ball.dx *= -1

            elif ball.gety() > 260:
                self.score1 += 1
                self.pen.clear()
                self.pen.write("Team 1: {}  Team 2: {} ".format(self.score1, self.score2), align="center",
                               font=("Courier", 19, "bold"))
                ball.reset()
                ball.dy *= -1

            elif ball.gety() < -260:
                self.score2 += 1
                self.pen.clear()
                self.pen.write("Team 1: {}  Team 2: {} ".format(self.score1, self.score2), align="center",
                               font=("Courier", 19, "bold"))
                ball.reset()
                ball.dy *= -1

        elif (self.gamemode == "4pRally"):
            if ball.getx() > 360:
                self.score1 = 0
                self.pen.clear()
                self.pen.write("Consecutive Hits: {} ".format(self.score1), align="center",
                               font=("Courier", 19, "bold"))
                ball.reset()
                ball.dx *= -1

            elif ball.getx() < -360:
                self.score1 = 0
                self.pen.clear()
                self.pen.write("Consecutive Hits: {} ".format(self.score1), align="center",
                               font=("Courier", 19, "bold"))
                ball.reset()
                ball.dx *= -1

            elif ball.gety() > 260:
                self.score1 = 0
                self.pen.clear()
                self.pen.write("Consecutive Hits: {} ".format(self.score1), align="center",
                               font=("Courier", 19, "bold"))
                ball.reset()
                ball.dy *= -1

            elif ball.gety() < -260:
                self.score1 = 0
                self.pen.clear()
                self.pen.write("Consecutive Hits: {} ".format(self.score1), align="center",
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

            # TOP BORDER
            elif ball.gety() > 250:
                ball.sety(250)
                ball.dy *= -1

            # BOTTOM BORDER
            elif ball.gety() < -250:
                ball.sety(-250)
                ball.dy *= -1

        elif (self.gamemode == "2pRally"):

            # RED PADDLE
            if ball.getx() < -317 and ball.gety() < self.paddle_a.gety() + 50 and ball.gety() > self.paddle_a.gety() - 50:
                # prevent side clipping
                ball.setx(-317)
                ball.dx *= -1
                self.score1 += 1
                self.pen.clear()
                self.pen.write("Consecutive Hits: {} ".format(self.score1), align="center",
                               font=("Courier", 19, "bold"))

            # BLUE PADDLE
            elif ball.getx() > 317 and ball.gety() < self.paddle_b.gety() + 50 and ball.gety() > self.paddle_b.gety() - 50:
                # prevent side clipping
                ball.setx(317)
                ball.dx *= -1
                self.score1 += 1
                self.pen.clear()
                self.pen.write("Consecutive Hits: {} ".format(self.score1), align="center",
                               font=("Courier", 19, "bold"))

            # TOP BORDER
            elif ball.gety() > 250:
                ball.sety(250)
                ball.dy *= -1

            # BOTTOM BORDER
            elif ball.gety() < -250:
                ball.sety(-250)
                ball.dy *= -1


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

        elif (self.gamemode == "4pRally"):

            # RED PADDLE
            if ball.getx() < -317 and ball.gety() < self.paddle_a.gety() + 50 and ball.gety() > self.paddle_a.gety() - 50:
                # prevent side clipping
                ball.setx(-317)
                ball.dx *= -1
                self.score1 += 1
                self.pen.clear()
                self.pen.write("Consecutive Hits: {} ".format(self.score1), align="center",
                               font=("Courier", 19, "bold"))

            # BLUE PADDLE
            elif ball.getx() > 317 and ball.gety() < self.paddle_b.gety() + 50 and ball.gety() > self.paddle_b.gety() - 50:
                # prevent side clipping
                ball.setx(317)
                ball.dx *= -1
                self.score1 += 1
                self.pen.clear()
                self.pen.write("Consecutive Hits: {} ".format(self.score1), align="center",
                               font=("Courier", 19, "bold"))

            # GREEN PADDLE
            elif ball.gety() > 230 and ball.getx() < self.paddle_c.getx() + 60 and ball.getx() > self.paddle_c.getx() - 60:
                # prevent side clipping
                ball.sety(230)
                ball.dy *= -1
                self.score1 += 1
                self.pen.clear()
                self.pen.write("Consecutive Hits: {} ".format(self.score1), align="center",
                               font=("Courier", 19, "bold"))

            # PURPLE PADDLE
            elif ball.gety() < -230 and ball.getx() < self.paddle_d.getx() + 60 and ball.getx() > self.paddle_d.getx() - 60:
                # prevent side clipping
                ball.sety(-230)
                ball.dy *= -1
                self.score1 += 1
                self.pen.clear()
                self.pen.write("Consecutive Hits: {} ".format(self.score1), align="center",
                               font=("Courier", 19, "bold"))

    
    def checkPaddleBounds(self):
        if(self.gamemode == "twoplayer" or self.gamemode == "2pRally"):
            if self.paddle_a.gety() >= 240:
                self.paddle_a.sety(225)
    
            elif self.paddle_a.gety() <= -240:
                self.paddle_a.sety(-225)

            if self.paddle_b.gety() >= 240:
                self.paddle_b.sety(225)

            elif self.paddle_b.gety() <= -240:
                self.paddle_b.sety(-225)


        elif(self.gamemode == "fourplayer" or self.gamemode == "4pRally"):
            if self.paddle_a.gety() >= 240:
                self.paddle_a.sety(225)
    
            elif self.paddle_a.gety() <= -240:
                self.paddle_a.sety(-225)

            if self.paddle_b.gety() >= 240:
                self.paddle_b.sety(225)

            elif self.paddle_b.gety() <= -240:
                self.paddle_b.sety(-225)

            if self.paddle_c.getx() >= 310:
                self.paddle_c.setx(310)

            elif self.paddle_c.getx() <= -310:
                self.paddle_c.setx(-310)

            if self.paddle_d.getx() >= 310:
                self.paddle_d.setx(310)

            elif self.paddle_d.getx() <= -310:
                self.paddle_d.setx(-310)
    
    
    
    def runGame(self):
        # TODO make the internal function
        while True:
            
            if(self.exit_flag):
                break

            self.win.update()

            for x in self.balls:

                x.move()
                # Scoring
                self.checkIfScore(x)

                #Collisions
                self.checkCollisions(x)

            #BoundsChecking    
            self.checkPaddleBounds()

            time.sleep(1/1000)

        self.win.bye()
        splashscreen.splashscreen() 


    def exitGame(self, x, y):
        self.exit_flag = 1



