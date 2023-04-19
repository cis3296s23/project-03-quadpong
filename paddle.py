
from turtle import Turtle



class paddle:
    def __init__(self, color, orientation, x, y):
        self.turtle = Turtle()
        self.orientation = orientation
        self.turtle.speed(3)
        self.turtle.shape("square")
        self.turtle.color(color)
        if(orientation == "v" or orientation == "V"):
            self.turtle.shapesize(stretch_wid=4,stretch_len=1)
        elif(orientation == "h" or orientation == "H"):
            self.turtle.shapesize(stretch_wid=1,stretch_len=4)
        else:
            print("Unknown orientation!!")
        self.turtle.penup()
        self.turtle.goto(x,y)


    def paddle_up(self):
        tempy = self.turtle.ycor()
        tempy += 50
        self.turtle.sety(tempy)


    def paddle_down(self):
        tempy = self.turtle.ycor()
        tempy -= 50
        self.turtle.sety(tempy)

    def paddle_left(self):
        x = self.turtle.xcor()
        x -= 50
        self.turtle.setx(x)    

    def paddle_right(self):
        x = self.turtle.xcor()
        x += 50
        self.turtle.setx(x)    