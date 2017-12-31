class rectangle:
    def __init__(self):
        return("inside of rectangle")

    def area(self,x,y):
        return x*y

class square(rectangle):
    def __init__(self):
        print("inside of a rectangle")

sq = square()
ans = sq.area(10,3)
print(ans)       