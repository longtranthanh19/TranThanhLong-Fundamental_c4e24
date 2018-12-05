items = ["T-Shirt", "Sweater"]
while True:
    cmd = input("Welcome to our shop, what do you want (C,R,U,D,E) ?")
    if cmd == "C":
        C = str(input("Enter new items "))
        items.append(C)
        print("Our Items" + str(items))
    elif cmd =="R":
        print("Our Items" + str(items))
    elif cmd =="U":
        n = int(input("Update Position ? "))
        t = str(input("New Items: "))
        items[n-1] = t
        print("Our Items" + str(items))
    elif cmd =="D":
        b = int(input("Delete Position ? "))
        items.pop(b-1) 
        print("Our Items" + str(items))            
    elif cmd =="E":
        break


