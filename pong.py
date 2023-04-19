# ___QUAD PONG___
#Domenic Malinsky 2023
#Credit For Christian Thompson @TokyoEdTech for the basic starter guide on 2 player pong.

import turtle
import os
import wave
import sys
import pygame
import time
import paddle
from tkinter import *

#song = wave.open("C:\Users\Domenic Malinsky\Desktop\Code\Python\GAME\ancients.mp3", "r")
#p = vlc.MediaPlayer("C:\Users\Domenic Malinsky\Desktop\Code\Python\GAME\ancients.mp3")
#p.play()
#os.system("afplay ancients.mp3")-mac(feels bad man)

title = Tk()
title.title("Quad Pong")
label_1 = Label(title, text = "Welcome To Pong")
label_2 = Label(title, text = "RULES")
label_3 = Label(title, text = "1. Control your paddle, [RIGHT: W UP, S DOWN], [LEFT UP ARROW UP, DOWN ARROW DOWN]")
label_4 = Label(title, text = "2. Get the ball to the opposite bound of the screen to score.")
label_5 = Label(title, text = "3. There is no score limit you can go for as long as you want do not stress over who wins it will take the focus away from the game.")
label_6 = Label(title, text = "Also the game has already started")
label_1.pack()
label_2.pack()
label_3.pack()
label_4.pack()
label_5.pack()
label_6.pack()

wn = turtle.Screen()
wn.title("Quad Pong")
wn.bgcolor("grey")
wn.setup(width=1000, height=800)
wn.tracer(0)

#Border
bd = turtle.Turtle()
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
paddle_a = paddle.paddle("red", "v", -340, 0)

#Paddle B
paddle_b = paddle.paddle("blue", "v", 340, 0)

#Paddle C
paddle_c = paddle.paddle("green", "h", 0, 250)

#Paddle D
paddle_d = paddle.paddle("purple", "h", 0, -250)


#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = 1

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 350)
pen.write("Player RED: 0  Player BLUE: 0", align="center", font=("Courier", 19, "bold"))


#Keyboard Bindings
wn.listen()

wn.onkeypress(paddle_a.paddle_up, "w")
wn.onkeypress(paddle_a.paddle_down, "s")
wn.onkeypress(paddle_b.paddle_up, "Up")
wn.onkeypress(paddle_b.paddle_down, "Down")

wn.onkeypress(paddle_c.paddle_left, "a")
wn.onkeypress(paddle_c.paddle_right, "d")
wn.onkeypress(paddle_d.paddle_left, "Left")
wn.onkeypress(paddle_d.paddle_right, "Right")



# ___MAIN___
while True:
    wn.update()
    
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

   
    