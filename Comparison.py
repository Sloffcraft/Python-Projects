#making comparison

name = input("Enter your name: ")

if len(name) < 4 :
    print("Name must be at least 4 characters long")
    
elif len(name) > 10:
    print("Name must be smaller than 10 characters")
    
else:
	print('Your name is Fine')