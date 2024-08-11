from turtle import *
draw=Turtle()

def draw_s(draw,size):
    draw.color("green")
    draw.begin_fill()
    draw.color('green')
    for i in range(4):
        draw.forward(size)
        draw.left(90)
    draw.end_fill()
    draw.penup()


def draw_rec(draw,width,height):
    draw.penup()
    draw.goto(-250, 0)
    draw.pendown()
    draw.color("red")
    draw.begin_fill()
    draw.color('red')
    draw.forward(width)
    draw.left(90)
    draw.forward(height)
    draw.left(90)
    draw.forward(width)
    draw.left(90)
    draw.forward(height)
    draw.end_fill()

draw_s(draw,200)
draw_rec(draw,200,100)
exitonclick()
