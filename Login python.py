def Login ():

  print("Please LOG IN")
print("what is your Username?  ")
Username = input("")
print("Hello " + Username)
print("what is your password?  ")
password = input("")
print("Finding account...")
if Username == "Rayyan" and password == "zxcvb" :
  print("Access granted")
break
else: 
  print("access denied")
  Choice1 = input("Would you like to create an account? ")
  choice2 = input("Would you like to log in? ")
  def Signin():
    print("Please sign in")
    print("First Name")
    FirstName = input("")
    print("Last Name")
    LastName = input("")
    print("Password")
    SPassword = input("")
    print("Email address")
    SEmailAddress = input("")
    SName = input("")
    print("password")

print("Welcome to our website")
Choice1 = input("Would you like to create an account? ")
choice2 = input("Would you like to log in? ")
if Choice1 == "yes":
  Signin()
else:
   Login()