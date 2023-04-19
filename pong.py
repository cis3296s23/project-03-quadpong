# ___QUAD PONG___
#Domenic Malinsky, Rishi Duggal, Tyler Grenell 2023


from turtle import Screen, Turtle
import os
import time
from gameObjs import paddle, ball



win = Screen()
win.title("Quad Pong")
win.bgcolor("dark grey")
win.setup(width=1000, height=800)
win.tracer(0)

#Border
bd = Turtle()
bd.penup()
bd.goto(-370,-270)
bd.pendown()
bd.pensize(5)
bd.fd(740)
bd.left(90)
bd.fd(540)
bd.left(90)
bd.fd(740)
bd.left(90)
bd.fd(540)
bd.hideturtle()

#Score
score_1 = 0
score_2 = 0

#Paddle A
paddle_a = paddle("red", "v", -340, 0)

#Paddle B
paddle_b = paddle("blue", "v", 340, 0)

#Paddle C
paddle_c = paddle("green", "h", 0, 250)

#Paddle D
paddle_d = paddle("purple", "h", 0, -250)


#Ball
ball_1 = ball(1)

#Pen
pen = Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 350)
pen.write("Team 1: 0  Team 2: 0", align="center", font=("Courier", 19, "bold"))


#Keyboard Bindings
win.listen()

win.onkeypress(paddle_a.paddle_up, "w")
win.onkeypress(paddle_a.paddle_down, "s")
win.onkeypress(paddle_b.paddle_up, "Up")
win.onkeypress(paddle_b.paddle_down, "Down")

win.onkeypress(paddle_c.paddle_left, "a")
win.onkeypress(paddle_c.paddle_right, "d")
win.onkeypress(paddle_d.paddle_left, "Left")
win.onkeypress(paddle_d.paddle_right, "Right")



# ___MAIN___
while True:
    win.update()
    
    #Ball Location
    ball_1.move()
    time.sleep(1/1000)

    #Scoring 
    if ball_1.getx() > 370:
        score_1 += 1
        pen.clear()
        pen.write("Team 1: {}  Team 2: {} ".format(score_1, score_2), align="center", font=("Courier", 19, "bold"))
        ball_1.reset()
        ball_1.dx *= -1

    elif ball_1.getx() < -370:
        score_2 += 1
        pen.clear()
        pen.write("Team 1: {}  Team 2: {} ".format(score_1, score_2), align="center", font=("Courier", 19, "bold"))
        ball_1.reset()
        ball_1.dx *= -1

    elif ball_1.gety() > 260:
        score_1 += 1
        pen.clear()
        pen.write("Team 1: {}  Team 2: {} ".format(score_1, score_2), align="center", font=("Courier", 19, "bold"))
        ball_1.reset()
        ball_1.dy *= -1
    
    elif ball_1.gety() < -260:
        score_2 += 1
        pen.clear()
        pen.write("Team 1: {}  Team 2: {} ".format(score_1, score_2), align="center", font=("Courier", 19, "bold"))
        ball_1.reset()
        ball_1.dy *= -1
    

    #bounds
    if paddle_a.gety() >= 240:
        paddle_a.sety(225)
    
    elif paddle_a.gety() <= -240:
        paddle_a.sety(-225)

    if paddle_b.gety() >= 240:
        paddle_b.sety(225)

    elif paddle_b.gety() <= -240:
        paddle_b.sety(-225)

    if paddle_c.getx() >= 310:
        paddle_c.setx(310)

    elif paddle_c.getx() <= -310:
        paddle_c.setx(-310)

    if paddle_d.getx() >= 310:
        paddle_d.setx(310)

    elif paddle_d.getx() <= -310:
        paddle_d.setx(-310)
    
    

    #Collision w Ball
    #RED PADDLE 
    if ball_1.getx() < -317 and ball_1.gety() < paddle_a.gety() + 50 and ball_1.gety() > paddle_a.gety() - 50:
        #prevent side clipping 
        ball_1.setx(-317)
        ball_1.dx *= -1 

    #BLUE PADDLE 
    elif ball_1.getx() > 317 and ball_1.gety() < paddle_b.gety() + 50 and ball_1.gety() > paddle_b.gety() - 50:
        #prevent side clipping 
        ball_1.setx(317)
        ball_1.dx *= -1

    # GREEN PADDLE
    elif ball_1.gety() > 230 and ball_1.getx() < paddle_c.getx() + 60 and ball_1.getx() > paddle_c.getx() - 60:
        #prevent side clipping 
        ball_1.sety(230)
        ball_1.dy *= -1

    # PURPLE PADDLE
    elif ball_1.gety() < -230 and ball_1.getx() < paddle_d.getx() + 60 and ball_1.getx() > paddle_d.getx() - 60:
        #prevent side clipping 
        ball_1.sety(-230)
        ball_1.dy *= -1


    #Paddle w Paddle 
    
    #TODO add proper paddle collision

   
    