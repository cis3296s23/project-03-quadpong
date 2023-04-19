import turtle
from tkinter import *



class paddle:
    MVMT_VALUE = 50
    def __init__(self, color, orientation, size, speed, x, y):
        self.turtle = turtle.Turtle()
        self.orientation = orientation
        self.x = x 
        self.y = y 
        self.turtle.speed(speed)
        self.turtle.shape("square")
        self.turtle.color(color)
        if(orientation == "v" or orientation == "V"):
            self.turtle.shapesize(stretch_wid=size,stretch_len=1)
        elif(orientation == "h" or orientation == "H"):
            self.turtle.shapesize(stretch_wid=1,stretch_len=size)
        else:
            print("Unknown orientation!!")
        self.turtle.penup()
        self.turtle.goto(x,y)
        self.turtle.pendown()

    def paddle_up(self):
        self.y = self.y + self.MVMT_VALUE
        self.turtle.penup()
        self.turtle.goto(self.x, self.y)
        self.turtle.pendown()


    def paddle_down(self):
        y = self.turtle.ycor()
        y -= self.MVMT_VALUE
        self.turtle.sety(y)

    def paddle_left(self):
        x = self.turtle.xcor()
        x -= self.MVMT_VALUE
        self.turtle.setx(x)    

    def paddle_right(self):
        x = self.turtle.xcor()
        x += self.MVMT_VALUE
        self.turtle.setx(x)    