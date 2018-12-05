while True:
    i = int(input("Guess my number (1-100): "))
    if i < 10:
        print("Oopss it's too small. Try again...")
    elif i < 19:
        print("You almost there. Try again...")
    elif i == 19:
        print("You got the number. Congrat...")
        break
    else:
        print("Oopss it's too large. Try again...")


    
    