
from turtle import Turtle
import random


class obj:
    """
        Basic object class, holds turtle obj and movement methods.
    """
    def __init__(self):
        """ Initializes turtle, 
        :return: nothing."""
        self.turtle = Turtle()

    def getx(self):
        """ maps getx from turtle to obj owned function, 
        :return: turtle.xcor()"""
        return self.turtle.xcor()
    
    def gety(self):
        """ maps gety from turtle to obj owned function, 
        :return: turtle.ycor()"""
        return self.turtle.ycor()
    
    def setx(self, x):
        """ maps setx from turtle to obj owned function, 
        :return: nothing"""
        self.turtle.setx(x)
    
    def sety(self, y):
        """ maps sety from turtle to obj owned function, 
        :return: nothing"""
        self.turtle.sety(y)


class paddle(obj):
    """Paddle class to represent onscreen paddle"""
    
    def __init__(self, color, orientation, x, y):
        """Initializes paddle.

            :param color: the color
            :param orientation: horizontal or vertical.
            :param x: starting x coord
            :param y: starting y coord
            
            :return: a paddle object
        """
        super().__init__()
        #init turtle obj and properties
        self.turtle.speed(3)
        self.turtle.shape("square")
        self.turtle.color(color)
        #init orientation to be vertical or horizontal.
        if orientation in ["v", "V"]:
            self.turtle.shapesize(stretch_wid=4,stretch_len=1)
        elif orientation in ["h", "H"]:
            self.turtle.shapesize(stretch_wid=1,stretch_len=5)
        else:
            print("Unknown orientation!!")
        #draw turtle object and place on coordinate grid.
        self.turtle.penup()
        self.turtle.goto(x,y)

    # movement controls 
    #TODO allow for user customizable paddle speed.
    def paddle_up(self):
        """ 
            moves paddle up via setting y up 50 px.
        """
        y = self.gety()
        y += 50
        self.sety(y)  

    def paddle_down(self):
        """ 
            moves paddle up via setting y down 50 px.
        """
        y = self.gety()
        y -= 50
        self.sety(y)  

    def paddle_left(self): 
        """ 
            moves paddle left via setting x down 50 px.
        """
        x = self.getx()
        x -= 50
        self.setx(x)  

    def paddle_right(self):
        """ 
            moves paddle right via setting x up 50 px.
        """
        x = self.getx()
        x += 50
        self.setx(x)

class ball(obj):
    """Representation of ball on screen.
    """
    def __init__(self, speed):
        """Creates a ball object and initializes it.

            speed (int): the multiplier of the ball speed.
            
            dx (int): the movement value of the ball on the x axis
            dy (int): the movement value of the ball on the y axis

        """
        super().__init__()
        self.turtle.speed(0)
        self.turtle.shape("circle")
        self.turtle.color("black")
        self.turtle.penup()
        self.turtle.goto(0, 0)
        self.dx = random.randint(1, 5) * speed
        self.dy = random.randint(1, 5) * speed
    
    def move(self):
        """Method to change the ball's position based on its own speed."""
        
        self.setx(self.getx() + self.dx)
        self.sety(self.gety() + self.dy)

    def reset(self):
        """Method to bring the ball back to the center of the screen"""
        self.turtle.goto(0,0)

class settingsObj:
    """Object to hold user settings
    """
    def __init__(self):
        """ Creates settings obj and initializes to base values
        """
        self.ball_speed = 1
        self.ball_count = 1
        self.points_to_win = 10
