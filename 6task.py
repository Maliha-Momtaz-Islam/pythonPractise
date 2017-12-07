#I = [2,18,22,17,24,8,12,27]

#print(list(filter(lambda x:x%3 == 0,I)))

def divisablebythree (I):
    print("the list is :", I)
    i = 0
    while(i<=len(I)):
        if (I[i]%3 == 0):
            print(I[i])
        i=i+1
    
#       print(I)
divisablebythree([2,18,22,17,24,8,12,27])