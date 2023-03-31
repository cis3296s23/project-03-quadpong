

title = Tk()
title.title("Quad Pong")
label_1 = Label(title, text = "Welcome To Quad Pong")
label_2 = Label(title, text = "RULES")
label_1.pack()
label_2.pack()

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