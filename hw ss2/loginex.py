print ("Welcome User")
print ("Please enter your Username: ")

name = raw_input()

username= "admin"

if name == username:
    print ("Correct. Please enter your password: ")

elif name != username:
    print ("Wrong, Closing Program")
    print(exit())

password= raw_input()
password1= "admin"

if password == (password1):
    print ("Correct. Logging in")
    print ("Welcome, " +username)

elif password != (password1):
    print ("Wrong, Closing Program")





