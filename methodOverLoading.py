class Rectangle:
    def __init__(self):
        print("inside a rectangle")

    def area(self,x,y):
        return x*y

class Square(Rectangle):
    def __init__(self):
        print("inside of a square")
    def area(self,x):
        return x**2

sq = Square()
print(sq.area(5))
print(sq.area(3,4))
