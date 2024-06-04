import random

def number_guesser(min_num, max_num):
    target_number = random.randint(min_num, max_num)
    attempts = 0

    while True:
        guess = int(input(f"Guess the number between {min_num} and {max_num}: "))
        attempts += 1

        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {target_number} correctly in {attempts} attempts.")
            break
number_guesser(1,100)