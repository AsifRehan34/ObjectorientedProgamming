import turtle
from turtle import *
def draw_triangle():
    for i in range(3):
        triangle.forward(100)
        triangle.left(120)
def draw_circle():
    turtle.circle(radius=30)



triangle=Turtle()
Circle = Turtle()
userinput=input("Circle or triangle:").lower()
if userinput=="triangle":
    draw_triangle()
elif userinput=="circle":
    draw_circle()
else:
    print("invalid input")
exitonclick()