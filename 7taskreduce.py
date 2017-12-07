from functools import reduce
I = [2,18,22,17,24,8,12,27]
print(reduce(lambda x,y:x+y,I))
print(reduce(lambda x,y:x*2+10,I))