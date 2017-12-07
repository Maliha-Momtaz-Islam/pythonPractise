import math
while 1:
    max = int(input("please input the highest number of the range starting from 2:  "))
    max += 1
    primes = range(2, max) 
    for i in range(2, int( math.ceil(math.sqrt(max)) )): 
        primes = list(filter(lambda x: x == i or x % i, primes))
    print (primes)