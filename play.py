while 1:
    x = int(input("please input an integer:"))
    if x<0:
        x=0
        print("negetive changed to zero")
    elif x == 0:
        print("zero")
    elif x==1:
        print("single")
    else:
        print("more")