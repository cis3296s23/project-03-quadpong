# ___QUAD PONG___
#Domenic Malinsky 2022
#Credit For Christian Thompson @TokyoEdTech for the basic starter guide on 2 player pong.

import turtle
import os
import wave
import pygame
import sys
import time
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
score_a = 0
score_b = 0

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(3)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=4,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-340, 0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(3)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=4,stretch_len=1)
paddle_b.penup()
paddle_b.goto(340, 0)


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
#Paddle A
def paddle_a_up():
    y = paddle_a.ycor()
    y += 50
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 50
    paddle_a.sety(y)

#Paddle B
def paddle_b_up():
    y = paddle_b.ycor()
    y += 50 
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 50
    paddle_b.sety(y)

def start_key():
    start = start_key

#Keyboard Bindings
wn.listen()

wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# ___MAIN___
while True:
    wn.update()
    
    #Ball Location
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    time.sleep(1/1000)

    #Scoring 
    if ball.xcor() > 370:
        score_a += 1
        pen.clear()
        pen.write("Player RED: {}  Player BLUE: {} ".format(score_a, score_b), align="center", font=("Courier", 19, "bold"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -370:
        score_b += 1
        pen.clear()
        pen.write("Player RED: {}  Player BLUE: {} ".format(score_a, score_b), align="center", font=("Courier", 19, "bold"))
        ball.goto(0, 0)
        ball.dx *= -1
    
    elif ball.ycor() > 260:
        ball.dy *= -1
    
    elif ball.ycor() < -260:
        ball.dy *= -1
    

    #Collision
    #RED PADDLE & BALL
    if ball.xcor() < -325 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1 

    #BLUE PADDLE & BALL
    elif ball.xcor() > 325 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
    
   #Testing Commit
        

   
    