#a new game idea has come out 
#'letter type'

#quit 
end = 0
end_limit = 1

#words to the question
word = 'sLOfFcRaFt'
word2 = 'sAmaXfLhA'

print('''Welcome ! To Letter type.
You have to enter same characters 
To proceed in an time limit under 5 sec''')

print(word)

user = ''

while end != end_limit:
    user = input('Enter the word: ')
    if user == word:
        end += 1
        print(word2)
        
    elif user != word:
        print('you lose try again !')
        break
        
    user = input('Enter second word: ')
    if user != word2:
        end += 1
        print('You lose try again !')
        break
    elif user == word2:
        print('You win !')