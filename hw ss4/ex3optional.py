from random import randint
word = "champion"
characters = list(word)

for _ in range(len(characters)):
    i = randint (0, len(characters) - 1)
    ch = characters[i]
    print(ch, end =" ")
    characters.pop(i)
print()
user_guess = input("Your guess? ")
if user_guess != word:
    print(":(")
else:
    print("Hura")
        
        

