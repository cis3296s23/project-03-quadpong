# ___QUAD PONG___
#Domenic Malinsky, Rishi Duggal, Tyler Grenell 2023


from turtle import Screen, Turtle
import os
import time
from Paddle import paddle



win = Screen()
win.title("Quad Pong")
win.bgcolor("grey")
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
ball = Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

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
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    time.sleep(1/1000)

    #Scoring 
    if ball.xcor() > 370:
        score_1 += 1
        pen.clear()
        pen.write("Team 1: {}  Team 2: {} ".format(score_1, score_2), align="center", font=("Courier", 19, "bold"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -370:
        score_2 += 1
        pen.clear()
        pen.write("Team 1: {}  Team 2: {} ".format(score_1, score_2), align="center", font=("Courier", 19, "bold"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.ycor() > 260:
        score_1 += 1
        pen.clear()
        pen.write("Team 1: {}  Team 2: {} ".format(score_1, score_2), align="center", font=("Courier", 19, "bold"))
        ball.goto(0, 0)
        ball.dy *= -1
    
    elif ball.ycor() < -260:
        score_2 += 1
        pen.clear()
        pen.write("Team 1: {}  Team 2: {} ".format(score_1, score_2), align="center", font=("Courier", 19, "bold"))
        ball.goto(0, 0)
        ball.dy *= -1
    

    #bounds
    if paddle_a.turtle.ycor() >= 240:
        paddle_a.turtle.sety(225)
    
    elif paddle_a.turtle.ycor() <= -240:
        paddle_a.turtle.sety(-225)

    if paddle_b.turtle.ycor() >= 240:
        paddle_b.turtle.sety(225)

    elif paddle_b.turtle.ycor() <= -240:
        paddle_b.turtle.sety(-225)

    if paddle_c.turtle.xcor() >= 320:
        paddle_c.turtle.setx(320)

    elif paddle_c.turtle.xcor() <= -320:
        paddle_c.turtle.setx(-320)

    if paddle_d.turtle.xcor() >= 320:
        paddle_d.turtle.setx(320)

    elif paddle_d.turtle.xcor() <= -320:
        paddle_d.turtle.setx(-320)
    
    

    #Collision w Ball
    #RED PADDLE 
    if ball.xcor() < -320 and ball.ycor() < paddle_a.turtle.ycor() + 50 and ball.ycor() > paddle_a.turtle.ycor() - 50:
        ball.dx *= -1 

    #BLUE PADDLE 
    elif ball.xcor() > 320 and ball.ycor() < paddle_b.turtle.ycor() + 50 and ball.ycor() > paddle_b.turtle.ycor() - 50:
        ball.dx *= -1

    # GREEN PADDLE
    elif ball.ycor() > 230 and ball.xcor() < paddle_c.turtle.xcor() + 50 and ball.xcor() > paddle_c.turtle.xcor() - 50:
        ball.dy *= -1

    # PURPLE PADDLE
    elif ball.ycor() < -230 and ball.xcor() < paddle_d.turtle.xcor() + 50 and ball.xcor() > paddle_d.turtle.xcor() - 50:
        ball.dy *= -1
        
    #Paddle w Paddle 
    
    #TODO add proper paddle collision

   
    