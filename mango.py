count = 1;
while 1:
    basket = int(input("how many basket of mango?"))
    for items in basket:
        x1 = int(input("how many mangoes in" + items + "basket?"))
        people = int(input("how many people you want to distribute to?"))
        if(x1%people==0):
            break
        else:
            continue

    



