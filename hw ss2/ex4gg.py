import sys
n = int(input("Enter n: "))
m = int(input("Enter m: "))
for row in range(m):
    for col in range(n):
        sys.stdout.write("*")
    print("*")