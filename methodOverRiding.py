class Rectangle:
    def __init__(self):
        print("inside a rectangle")

    def area(self,x,y):
        return x*y

class Square(Rectangle):
    def __init__(self):
        print("inside of a square")

    def area(self,x):
        return Rectangle.area(self,x,x)

sq = Square()
print(sq.area(5))
