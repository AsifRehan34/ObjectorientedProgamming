from turtle import *
def hexagone():

    # create turtle object
    myturtle=Turtle()
    myturtle.fillcolor('green')
    myturtle.begin_fill()
    # use forward method to move turtle forward 100 points
    myturtle.forward(100)
    # move turtle left 60 degrees
    myturtle.left(60)

    # repeat the same process five times
    myturtle.forward(100)
    myturtle.left(60)
    myturtle.forward(100)
    myturtle.left(60)
    myturtle.forward(100)
    myturtle.left(60)
    myturtle.forward(100)
    myturtle.left(60)
    myturtle.forward(100)
    myturtle.left(60)
    myturtle.end_fill()
    exitonclick()
hexagone()