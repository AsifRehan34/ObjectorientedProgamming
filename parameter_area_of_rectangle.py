class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def rectangle_info(self):
        print(self.length)
        print(self.width)

    def parameter(self):
        parameter = (self.length + self.width) * 2
        self.parameter = parameter
        return self.parameter

    def area(self):
        area = self.length * self.width
        self.area = area
        return self.area

    def update(self, length):
        self.updated = (self.length - length) * self.width
        return self.updated


length = int(input("Enter the length of rectangle: "))
width = int(input("Enter the width of the rectangle: "))

myrectangle = Rectangle(length, width)
myrectangle.rectangle_info()
print("the parameter of the rectangle is: ", myrectangle.parameter())
print("the area of the rectangle is :", myrectangle.area())
update_length = int(input("enter length you want to reduce: "))
print("updated area: ", myrectangle.update(update_length))
