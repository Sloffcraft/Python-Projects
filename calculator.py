#making a calculator 
#idk how to do that hust practicing my skills and some if elif and else statements

user_command = ""

while user_command != "quit":
    user_command = int(input("Enter first number: "))
    user_command2 = int(input("Enter second number: "))
    
    print('''Add -  a 
subtract - s 
divide - d 
multiple - m ''')
    
    operators = str(input("Enter one of the alphabet characters: ")).lower()
    
    if operators == "a":
        result = user_command + user_command2
        print(f"Your added value is {result}.")
        
    elif operators == "s":
        result = user_command - user_command2
        print(f"Your subtracted value is {result}.")
        
    elif operators == "d":
         result = user_command / user_command2
         print(f"Your divided divident is {result}.")
         
    elif operators == "m":
         result = user_command * user_command2
         print(f"Your multiplied value is {result}.")
         
else:
    print("You at least have to type a number")