from turtle import *
# create object of triangel 1
triangle=Turtle()
# set the dimension to draw triangle
triangle.goto(-120,0)
# set the fill color
triangle.fillcolor('green')
# start the filling color
triangle.begin_fill()
# repeat the process three times at an agle of 120
for i in range(3):
    triangle.forward(200)
    triangle.left(120)
triangle.end_fill()
# pull up the pen to move the pen to other position and then draw other triangle
triangle.penup()

triangle2=Turtle()
triangle2.fillcolor('red')
triangle2.begin_fill()
triangle2.penup()
triangle2.goto(0,-200)
triangle2.pendown()
for i in range(3):
    triangle2.forward(200)
    triangle2.left(120)
triangle2.end_fill()
triangle2.penup()

triangle3=Turtle()
triangle3.fillcolor('yellow')
triangle3.begin_fill()
triangle3.penup()
triangle3.goto(-220,-200)
triangle3.pendown()
for i in range(3):
    triangle3.forward(200)
    triangle3.right(240)
triangle3.end_fill()
exitonclick()