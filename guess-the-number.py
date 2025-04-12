import random

def guess_the_number():
    print("Welcome to 'Guess the Number'!")
    print("I am thinking of a number between 1 and 100.")
    print("Can you guess what it is?")
    
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False
    
    while not guessed_correctly:
        try:
            # Prompt the user for a guess
            user_guess = int(input("Enter your guess: "))
            attempts += 1
            
            if user_guess < number_to_guess:
                print("Too low !")
            elif user_guess > number_to_guess:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts!")
                guessed_correctly = True
        except ValueError:
            print("Please enter a valid number.")
    
    print("Thank you for playing!")

# Run the game
if __name__ == "__main__":
    guess_the_number()
