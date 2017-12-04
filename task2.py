while 1:
    x = int(input("please input an integer number:"))
    if x<0:
        print("negetive number detected")
    elif x==0:
        print("negetive changed to zero")
    elif x%2 == 0:
        print("this is even number")
    elif x%2 != 0:
        print("this is odd number")
    else:
        print("error")