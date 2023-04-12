import turtle
from tkinter import *



class paddle:
    MVMT_VALUE = 50
    obj = turtle.Turtle()

    def __init__(self, color, orientation, size, speed, x, y):
        self.orientation = orientation
        self.x = x 
        self.y = y 
        self.obj.speed(speed)
        self.obj.shape("square")
        self.obj.color(color)
        if(orientation == "v" or orientation == "V"):
            self.obj.shapesize(stretch_wid=size,stretch_len=1)
        elif(orientation == "h" or orientation == "H"):
            self.obj.shapesize(stretch_wid=1,stretch_len=size)
        else:
            print("Unknown orientation!!")
        self.obj.penup()
        self.obj.goto(x,y)

    def paddle_up(self):
        y = self.obj.ycor()
        print()
        y += self.MVMT_VALUE
        self.obj.sety(y)


    def paddle_down(self):
        y = self.obj.ycor()
        y -= self.MVMT_VALUE
        self.obj.sety(y)

    def paddle_left(self):
        x = self.obj.xcor()
        x -= self.MVMT_VALUE
        self.obj.setx(x)    

    def paddle_right(self):
        x = self.obj.xcor()
        x += self.MVMT_VALUE
        self.obj.setx(x)    