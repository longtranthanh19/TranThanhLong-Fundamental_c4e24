from random import *
er = randint(-1,1)

def generate_quiz():
    # Hint: Return [x, y, op, result]
    x = randint(1,10)
    y = randint(1,10)
    op = choice(["+","-","*","/"])
    result = 0
    if op == "+":
        result = x + y + er
    elif op == "-":
        result = x - y + er
    elif op == "*":
        result = x * y + er 
    elif op == "/": 
        result = x / y + er
    return x, y, op, result 
    
    
def check_answer(x, y, op, result, user_choice):
    print(user_choice)
    a = generate_quiz()
    x = a[0]
    y = a[1]
    op = a[2]
    r = a[3]

    if op == "+":
        er = r - x -y
    elif op == "-":
        er = r - x + y
    elif op == "*":
        er = r - x * y
    elif op == "/":
        er = r - x / y

    if er == 0:
        if user_choice == True:
            return True
        elif user_choice == False:
            return False
    else:
        if user_choice == True:
            return False
        elif user_choice == False:
            return True
    
    
        

        
