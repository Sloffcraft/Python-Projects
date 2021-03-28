#making a comparision meter

first_name = input('Enter first name: ')

fav_number = int(input('Enter a fav. number: '))

second_name = input('Enter second name: ')

value = len(first_name) / len(second_name) * fav_number

if value > 50.0:
    print(f'Your percentage is {value}')
else :
    print(f'Low Percentage {value}.')