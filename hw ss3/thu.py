from random import randint
n = randint(1, 100)

while True:
    m = int(input("Guess my number (1-100)? "))
    if m < n:
        print("Too small :(")
    elif m > n:
        print("A little too large :(")
    else:
        print("Bingo")
        break