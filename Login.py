#making a login interface 

username = "sloffcraft"
code = "kid123meht"
codin = ""

input_user = input("Enter your username: ")

if input_user == username :
    codin = input("Enter your Password: ")
   
if codin == code :
    print('''Welcome back 
sir i hope you have a nice day''')
     
elif codin != code :
   print("Something went wrong please check password or username and Try again !")
   
else :
    print("At least you have to type a name or password")