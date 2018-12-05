import sys
i = 1 
while i <= 9:
    sys.stdout.write("x")
    i = i +1
    if i <= 9:
        sys.stdout.write("*")
        i = i + 1
    else:
        exit()