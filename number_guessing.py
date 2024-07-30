import random

lower_bound = int(input("The lower bound: "))
upper_bound = int(input("The upper bound: "))


secret_number = random.randint(lower_bound,upper_bound)
guess = 0

while 1:
    guess = int(input("Your guess: "))
    if guess == secret_number:
        print(f"You guessed correctly! The number was {guess}")
        break
    else:
        if guess > secret_number:
            print("The number must be smaller")
        else:
            print("The number must be bigger")