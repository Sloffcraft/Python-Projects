#making better weight system 

weight = int(input("Weight: "))
inworl = input("Is it in (P)pounds or (k)kilo: ")

if inworl.upper() == "P":
    result =  weight*0.45
    print(f"In kilo: {result}")
    
elif inworl.upper() == "K":
    result = weight/0.45
    print(f"In pounds: {result}")
    
else :
    print("You have to choose.")