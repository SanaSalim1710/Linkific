import random
number = random.randint(0,10)
guess_count = 1

while True:
    guess = int(input("Guess the number!: "))
    if guess == number:
        break
    else:
        print("Try again")
        guess_count += 1

print(f"Correct! It took {guess_count} tries to guess the right number.")

