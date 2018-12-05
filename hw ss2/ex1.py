h = float(input("Enter your height:(m)"))
w = float(input("Enter your weight:(kg)"))
BMI = w/(h*h)
print("Your BMI is: " + str(BMI))
if BMI < 16:
    print("You're Severely Underweight")
elif BMI < 18.5:
    print("You're Underweight")
elif BMI < 25:
    print("You're Normal")
elif BMI < 30:
    print("You're Overweight")
else:
    print("You're Obese")
