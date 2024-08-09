from turtle import *
myturtle=Turtle()
myturtle.width(5)
myturtle.fillcolor("red")
myturtle.begin_fill()
for i in range(6):
    myturtle.forward(100)
    myturtle.left(60)
myturtle.end_fill()
exitonclick()