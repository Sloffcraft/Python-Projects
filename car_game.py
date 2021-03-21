#making a car 
#test no. 3

user_input = str(input("> "))

while user_input.upper() != "QUIT":
    if user_input.upper() == "START":
        print("Car is start...ready to go")
        user_input = str(input("> "))
       
    if user_input.upper() == "STOP" or user_input.upper() == "QUIT":
          print("Your car has been stopped ")
          user_input = str(input("> "))
          
    if user_input.upper() == "HELP":
          print(" start - start the car \n stop - stop the car \n quit - to exit ")
          user_input = str(input("> "))
          
    if user_input.upper() == "QUIT":
        print("It has been closed")
        break
          
    else :
        print("I don't understand that 'help' for wome instructions")
        user_input = str(input("> "))