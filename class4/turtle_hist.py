# -*- coding: UTF-8 -*-
import turtle
# myTurtle = turtle.Turtle()
from turtle import *
def doBar(height, clr):
    begin_fill()
    color(clr)
    setheading(90)
    forward(height)
    right(90)
    forward(40)
    right(90)
    forward(height)
    end_fill()

values = [49, 118, 201, 241, 168, 266, 221, 65, 231]
colors = ["green", "blue", "red", "yellow", "orange", "purple", "black",
          "pink", "grey"]
up()
goto(-300, -200)
down()
idx = 0
for value in values:
    doBar(value, colors[idx])
    idx += 1

done()