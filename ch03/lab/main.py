import turtle #1. import modules
import random

#Part A
window = turtle.Screen() # 2
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)



window.exitonclick()
