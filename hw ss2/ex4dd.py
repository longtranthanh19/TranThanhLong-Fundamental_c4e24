import sys
n = int(input("Enter a number: "))
import sys
i = 1 
while i <= n:
    sys.stdout.write("x")
    i = i +1
    if i <= n:
        sys.stdout.write("*")
        i = i + 1
    else:
        exit()