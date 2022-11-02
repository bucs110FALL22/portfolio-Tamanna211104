▼
▼
▼
▼
#Setup
import turtle
import random
import time
from time import sleep
sleep(3)
sm = turtle.Screen()
sm.setup(800, 600)
t = turtle.Turtle()
sm.bgcolor("blue")
t.hideturtle()
sm.tracer(0)
loop = True
#Adding your turtle
cturtle = turtle.Turtle()
cturtle.shape("turtle")
cturtle.color("green")
cturtle.turtlesize(3, 3, 3)
cturtle.penup()
#Adding bot turtles
#Bot1
b1 = turtle.Turtle()
b1.penup()
b1.shape("turtle")
b1.color("purple")
b1.turtlesize(3, 3, 3)
b1.goto(-314, 29)
b1.left(135)
#Bot2
b2 = turtle.Turtle()
b2.penup()
b2.shape("turtle")
b2.turtlesize(3, 3, 3)
b2.goto(314, -292)
b2.left(234)
#Bot3
b3 = turtle.Turtle()
b3.penup()
b3.shape("turtle")
b3.color("red")
b3.turtlesize(3, 3, 3)
b3.goto(-452, 27)
b3.left(234)
#Adding def for your turtle
def forward():
    cturtle.forward(50)
def left():
    cturtle.left(45)
def right():
    cturtle.right(45)
#Adding keybinds to your turtle
turtle.listen()
sm.onkeypress(forward, "w")
sm.onkeypress(left, "a")
sm.onkeypress(right, "d")
#Adding movement to bot turtles - 3 bots - num1 - num6
sm.tracer(1)
while (loop):
    num1 = random.randint(1, 40)
    num2 = random.randint(1, 40)
    num3 = random.randint(1, 40)
    num4 = random.randint(1, 40)
    num5 = random.randint(1, 40)
    num6 = random.randint(1, 40)
    b1.forward(num1)
    b1.right(num2)
    b1.forward(num3)
    b1.right(num4)
    b1.forward(num5)
    b1.left(num6)#Bot2 =
    b2.forward(num4)
    b2.right(num6)
    b2.forward(num1)
    b2.right(num5)
    b2.forward(num2)
    b2.left(num3)#Bot3
    b3.forward(num6)
    b3.right(num5)
    b3.forward(num3)
    b3.right(num2)
    b3.forward(num1)
    b3.left(num4)
    
    





turtle.done()