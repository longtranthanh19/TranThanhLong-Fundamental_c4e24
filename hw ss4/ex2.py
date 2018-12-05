#Ex2.1 
print("Hello my name is Long and there are my sheeps sizes:")
sizes = [5, 7, 300, 90, 2, 50, 75]
print(sizes)
#Ex2.2
m = max(sizes)
print("Now the biggest sheep has size " + str(m) + " let's shear it")
#Ex2.3
sizes.remove(m)
sizes.append(8)
print("After shearing, here is my flock")
print(sizes)
#Ex2.4
for i in range(len(sizes)):
    sizes[i] = sizes[i] + 50
print("One month has passed, now here is my flock")
print(sizes)
print("**************************************************************")

#Ex2.5
u = int(input("Enter The Number Of Months You Want To See ?"))
for i in range(1,u+1):
    print("MONTH " , i , end = ":")
    print()

    for j in range(len(sizes)):
        sizes[j] = sizes[j] + 50
    print("One month is passed, now here is my flock: ")
    print(sizes)

    n = max(sizes)
    print("Now my biggest sheep has sizez ", n, " let's shear it")
    
    sizes.remove(n)
    sizes.append(8)
    print("After shearing, here is my flock: ")
    print(sizes)
    print()

#Ex2.6
sizes_sum = sum(sizes)
print("My flock has sizes in total: ", sizes_sum)
money = sizes_sum * 2
print("I would get ", sizes_sum, end = " * 2$ = ")
print(money)
