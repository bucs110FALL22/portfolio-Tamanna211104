# CS110 Midterm Exam

## SHORT DESCRIPTION *(penguin drawing using functions and turtle module)*

## KNOWN BUGS AND INCOMPLETE PARTS *(I find it difficult to get the penguin to move around and the console says unable to run, main file ".replit" not found )*

## REFERENCES *(free code camp youtube tutorials)*

## MISCELLANEOUS COMMENTS *(I may be facing some issue with the platform of repl as I unable to run the code, I also have not recieved any response from the TA or my Professor on Discord)*

from turtle import *
'''
#movement
turtle.forward(100)
turtle.backward(200)
turtle.goto(100,100)

#pen control
turtle.penup()
turtle.goto(-100,100)
turtle.pendown()
turtle.goto(-100,0)

#angle, degrees
turtle.left(90)
turtle.right(90)
turtle.setheading(270)

#circle
#circle(50)
#draws a circle that is 50 in radius 
turtle.circle(50,180)

#color
turtle.fillcolor("pink")
turtle.pencolor("blue")
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

#stamp
turtle.stamp()
turtle.forward(100)
turtle.stamp()
turtle.forward(100)
'''
#body
turtle.setheading(270)
turtle.turtle.begin_fill()
turtle.circle(50,180)
turtle.forward(80)
turtle.circle(50,180)
turtle.forward(80)
turtle.end_fill()

#belly
turtle.fillcolor("white")
turtle.goto(10,0)
turtle.begin_fill()
turtle.circle(40)
turtle.end_fill()

#eyes
turtle.setheading(0)
turtle.goto(30,80)
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()
turtle.goto(70,80)
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()

turtle.shape("circle")
turtle.fillcolor("black")
turtle.penup()
turtle.goto(30,100)
turtle.stamp()
turtle.goto(70,100)
turtle.stamp()

#beak
turtle.shape("triangle")
turtle.fillcolor("orange")
turtle.goto(50,70)
turtle.setheading(270)
turtle.stamp()

#flippers
turtle.fillcolor("black")
turtle.pencolor("white")
turtle.setheading(0)
turtle.goto(0,50)
turtle.stamp()
turtle.setheading(180)
turtle.goto(100,50)
turtle.stamp()

#feet
turtle.shape("square")
turtle.fillcolor("orange")
turtle.goto(35,-50)
turtle.stamp()
turtle.goto(65,-50)
turtle.stamp()