from turtle import *
drawing=Turtle()
def draw_triangle(drawing,size,angle):
    for i in range(3):
        drawing.forward(size)
        drawing.left(angle)
def draw_circle(drawing,radius):
    drawing.circle(radius)

userinput=input("Circle or triangle:").lower()
if userinput=="triangle":
    draw_triangle(drawing,200,90)
elif userinput=="circle":
    draw_circle(drawing,50)
else:
    print("invalid input")
exitonclick()