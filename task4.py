import math 
n = int(input("input:"))
# method to print the divisors
def printDivisors(n) :
    i = 1
    while i <= math.sqrt(n) + 1 :
        if (n % i == 0) :
            # If divisors are equal, print only one
            if (n / i == i) :
                print (i)
            else :
                # Otherwise print both
                print (i , n/i)
        i = i + 1
printDivisors(n)