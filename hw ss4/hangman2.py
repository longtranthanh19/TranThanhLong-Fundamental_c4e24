from random import randint

name = input("What is your name ?")

print("Welcome " + name + " to Hangman: ")  

print("Start guessing... ")

n = 0 
er = 0 
blank_space = []

while True:
    if er > 0:
        print("---|")
    else:
        print("---")
    if er > 1:
        print("   |")
    else:
        print()
    if er > 2:
        print("   o")
    else:
        print()
    if er > 3:
        print("  -", end = "")
    else:
        print()
    if er > 4:
        print("|", end ="")
    else:
        print()
    if er > 5:
        print("-")
    else:
        print()
    if er > 6:
        print("  /", end = "")
    else: 
        print()
    if er == 8:
        print("|")
    else:
        print()
    print()
    print()
    print()

    if er ==8:
        print("You lose :( ")
        break

    if n == 0:
        wordl = ["TranThanhLong", "techkids", "python", "difficult"]
        j = randint(0,len(wordl)-1)
        word = wordl[j]
        n = n + 1


    if n == 1:
            for i in range(len(word)):
                blank_space.append("_")
                n = n +1             

    print(*blank_space)
    print()

    guess = str(input("Your guess? "))
    
    k = 0
    characters = list(word)
    for i in range(len(characters)):
        if guess == characters[i]:
            blank_space[i] = guess
        else:
            k = k + 1               

    if k == len(characters):                
        er = er + 1                      
    
    if blank_space == characters:
        print("You win^^")
        break 



    

