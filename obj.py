#str = " hello IoT Lab   "

#l = len(str)

#print(l)
#print(str.strip())
#print(str)

#========================

#class square:
#    side = 0
#    def area(self):
#        return self.side * self.side

#sq = square()
#sq.side = 5
#ans = sq.area()
#print(ans)
#===================

class square:
    def __init__(self,x):
        self.side = x
    def area(self):
        return self.side * self.side

sq = square(10)
ans = sq.area()
print(ans)