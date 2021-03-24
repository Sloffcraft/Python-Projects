#making a car 

# Improvements by Rohit Mehta (@mrohit-dev)
started = False

while True:
    user_input = input("> ").upper()
    
    if user_input == "START":
        if started:
            print("Car is already started")
        print("Car is starting...Ready to Go !!!")
        
    elif user_input == "STOP":
          if not started:
              print("Car is already stopped")
          print("Car Stopped ∆")
          
    elif user_input == "HELP":
          print ('Command List (Not case-sensitive):')
          print("    start - start the car\n    stop - stop the car\n    quit - to exit\n")
          
    elif user_input == "QUIT":
        print("Quitting...")
        break

    else:
        print("I didn't understand!\nType 'help'")