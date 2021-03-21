#making a guess game dk how to make it well but just trying

secret_code = 9
guess_count = 0
guess_chance = 3

while guess_count < guess_chance:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_code:
        print("You won")
        break
else:
    print("You lose")