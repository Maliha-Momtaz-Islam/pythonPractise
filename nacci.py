def fib(n):
    a,b = 2,3
    while a < n :
        print(b+1)
        a, b = b , a+b
        print("a is now:",a)
        print("b is now:", b)

fib(50)