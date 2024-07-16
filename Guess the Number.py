import random

def guess_the_number():
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")

    target_number = random.randint(1, 100)
    max_attempts = 10
    attempts = 0

    while attempts < max_attempts:
        guess = int(input("Enter your guess (1-100): "))
        attempts += 1

        if guess == target_number:       
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            return
        elif guess < target_number:
            if guess == target_number - 1:
                print("Your guess is very close.")
            else:
                print("Your guess is too low. Try a higher number.")
        else:
            if guess == target_number + 1:
                print("Your guess is very close.")
            else:
                print("Your guess is too high. Try a lower number.")

    print(f"Game over! The number was {target_number}.")

def main():
    guess_the_number()

if __name__ == "__main__":
    main()