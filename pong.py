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
pad_a = paddle.paddle("red", "v", 4, 3, -340, 0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(3)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=4,stretch_len=1)
paddle_b.penup()
paddle_b.goto(340, 0)

#Paddle C
paddle_c = turtle.Turtle()
paddle_c.speed(3)
paddle_c.shape("square")
paddle_c.color("green")
paddle_c.shapesize(stretch_wid=1,stretch_len=4)
paddle_c.penup()
paddle_c.goto(0, 250)

#Paddle D
paddle_d = turtle.Turtle()
paddle_d.speed(3)
paddle_d.shape("square")
paddle_d.color("purple")
paddle_d.shapesize(stretch_wid=1,stretch_len=4)
paddle_d.penup()
paddle_d.goto(0, -250)


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

# ---Moving Paddles--- 
# Numbers mean how many increments the paddle moves for respective paddle direction.

#Paddle B
def paddle_b_up():
    y = paddle_b.ycor()
    y += 50
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 50
    paddle_b.sety(y)

#Paddle C
def paddle_c_right():
    x = paddle_c.xcor()
    x += 50
    paddle_c.setx(x)

def paddle_c_left():
    x = paddle_c.xcor()
    x -= 50
    paddle_c.setx(x)

#Paddle D
def paddle_d_right():
    x = paddle_d.xcor()
    x += 50
    paddle_d.setx(x)

def paddle_d_left():
    x = paddle_d.xcor()
    x -= 50
    paddle_d.setx(x)

def start_key():
    start = start_key

#Keyboard Bindings
wn.listen()

wn.onkeypress(pad_a.paddle_up(), "w")
wn.onkeypress(pad_a.paddle_down(), "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

wn.onkeypress(paddle_c_left, "a")
wn.onkeypress(paddle_c_right, "d")
wn.onkeypress(paddle_d_left, "Left")
wn.onkeypress(paddle_d_right, "Right")



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
    if pad_a.turtle.ycor() >= 240:
        pad_a.turtle.sety(225)
    
    elif pad_a.turtle.ycor() <= -240:
        pad_a.turtle.sety(-225)

    if paddle_b.ycor() >= 240:
        paddle_b.sety(225)

    elif paddle_b.ycor() <= -240:
        paddle_b.sety(-225)

    if paddle_c.xcor() >= 320:
        paddle_c.setx(320)

    elif paddle_c.xcor() <= -320:
        paddle_c.setx(-320)

    if paddle_d.xcor() >= 320:
        paddle_d.setx(320)

    elif paddle_d.xcor() <= -320:
        paddle_d.setx(-320)
    
    

    #Collision w Ball
    #RED PADDLE 
    if ball.xcor() < -320 and ball.ycor() < pad_a.y + 50 and ball.ycor() > pad_a.y - 50:
        ball.dx *= -1 

    #BLUE PADDLE 
    elif ball.xcor() > 320 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1

    # GREEN PADDLE
    elif ball.ycor() > 230 and ball.xcor() < paddle_c.xcor() + 50 and ball.xcor() > paddle_c.xcor() - 50:
        ball.dy *= -1

    # PURPLE PADDLE
    elif ball.ycor() < -230 and ball.xcor() < paddle_d.xcor() + 50 and ball.xcor() > paddle_d.xcor() - 50:
        ball.dy *= -1
        
    #Paddle w Paddle 
    
    #TODO add proper paddle collision

   
    