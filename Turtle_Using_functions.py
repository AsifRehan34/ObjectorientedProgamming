from turtle import *
def draw_s():
    square.color("green")
    square.begin_fill()
    square.color('green')
    for i in range(4):
        square.forward(200)
        square.left(90)
    square.end_fill()
    square.penup()


def draw_rectangle():
    rectangle.penup()
    rectangle.goto(-250, 0)
    rectangle.pendown()
    rectangle.color("red")
    rectangle.begin_fill()
    rectangle.color('red')
    rectangle.forward(200)
    rectangle.left(90)
    rectangle.forward(100)
    rectangle.left(90)
    rectangle.forward(200)
    rectangle.left(90)
    rectangle.forward(100)
    rectangle.end_fill()

square=Turtle()
draw_s()
rectangle = Turtle()
draw_rectangle()
exitonclick()
