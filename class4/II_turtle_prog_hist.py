# -*- coding: UTF-8 -*-
# 2、按给定的进步率，画出每月进步的柱状效果图；

'''
补充知识：复利：小明到银行存1000元，打算存4年，年利息是4%，每年复利4次，
那么4年后，小明最后得到钱就是：1000×（1+4%/4）^4*4=1172.578元单利：
同样的例子，只是复利变成了单利，那么小明最后得到的钱就是：
1000*(4%/4）*4*4+1000=1160元
此处算复利
'''
from turtle import *

def drawAxis(length, angle, clr):
    axis = Turtle()
    # Initialization of turtle - arrow
    axis.penup()
    axis.goto(-300, -200)
    axis.pendown()
    axis.color(clr)
    axis.pensize(6)
    # rotate 'angle' degrees anticlockwise
    axis.left(angle)
    # the road is 200 pixles
    axis.forward(length)

def drawBar(width, height, clr):
    begin_fill()
    color(clr)
    setheading(90)
    forward(height)
    right(90)
    forward(width)
    right(90)
    forward(height)
    end_fill()

# wn = turtle.Screen()

# monthfactor = 0.2
monthfactor = float(input("Monthly progress rate: "))

# x-axis
drawAxis(250, 90, "black")
# y-axis
drawAxis(500, 0, "black")

# The color of each Column strip - 12 months
colors = ["green", "blue", "red", "yellow", "orange", "purple", "black",
          "pink", "grey", "green", "blue", "red"]

penup()
goto(-300, -200)
pendown()
width = 40
for imonth in range(1, 13):
    inc = 20 * (1 + (1 + monthfactor) ** imonth)
    drawBar(width, inc, colors[imonth-1])

penup()
goto(-300, 60)
pendown()
color("black")
write("The progress of learing monthly",
      font=("Arial", 26, "normal"))

done()