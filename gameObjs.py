
from turtle import Turtle
import random


class obj:
    def __init__(self):
        self.turtle = Turtle()

    def getx(self):
        return self.turtle.xcor()
    
    def gety(self):
        return self.turtle.ycor()
    
    def setx(self, x):
        self.turtle.setx(x)
    
    def sety(self, y):
        self.turtle.sety(y)


class paddle(obj):
    def __init__(self, color, orientation, x, y):
        super().__init__()
        #init turtle obj and properties
        self.turtle.speed(3)
        self.turtle.shape("square")
        self.turtle.color(color)
        #init orientation to be vertical or horizontal.
        if(orientation == "v" or orientation == "V"):
            self.turtle.shapesize(stretch_wid=4,stretch_len=1)
        elif(orientation == "h" or orientation == "H"):
            self.turtle.shapesize(stretch_wid=1,stretch_len=5)
        else:
            print("Unknown orientation!!")
        #draw turtle object and place on coordinate grid.
        self.turtle.penup()
        self.turtle.goto(x,y)

    # movement controls 
    #TODO allow for user customizable paddle speed.
    def paddle_up(self):
        y = self.gety()
        y += 50
        self.sety(y)  

    def paddle_down(self):
        y = self.gety()
        y -= 50
        self.sety(y)  

    def paddle_left(self):
        x = self.getx()
        x -= 50
        self.setx(x)  

    def paddle_right(self):
        x = self.getx()
        x += 50
        self.setx(x)

class ball(obj):
    def __init__(self, speed):
        super().__init__()
        self.turtle.speed(0)
        self.turtle.shape("circle")
        self.turtle.color("black")
        self.turtle.penup()
        self.turtle.goto(0, 0)
        self.dx = random.randint(1, 3) * speed
        self.dy = random.randint(1, 3) * speed
    
    def move(self):
        self.setx(self.getx() + self.dx)
        self.sety(self.gety() + self.dy)

    def reset(self):
        self.turtle.goto(0,0)

class settingsObj:
    def __init__(self):
        self.ball_speed = 1
        self.ball_count = 1
        self.points_to_win = 10
