from turtle import Turtle,Screen
timm=Turtle()
def moveF():
    timm.forward(20)
def moveB():
    timm.backward(20)
def turnL():
    newHeading = timm.heading()+20
    timm.setheading(newHeading)
def turnR():
    newHead= timm.heading()-20
    timm.setheading(newHead)
def clear():
    timm.clear()
    timm.penup()
    timm.home()
    timm.pendown()
screen=Screen()
screen.listen()
screen.onkey(key="w", fun=moveF)
screen.onkey(key="s", fun=moveB)
screen.onkey(key="a", fun=turnL)
screen.onkey(key="d", fun=turnR)
screen.onkey(key="c",fun=clear)
screen.exitonclick()